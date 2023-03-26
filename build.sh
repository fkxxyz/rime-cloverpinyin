#!/usr/bin/env bash
set -e

SHELLDIR="$(dirname "$(readlink -f "$0")")"


minfreq="${1:-100}"

mkdir -p "$SHELLDIR/cache"
cd "$SHELLDIR/cache"

# 生成符号列表
mkdir -p opencc
(
  cd opencc
  ../../rime-symbols/rime-symbols-gen
)

# 生成符号词汇
cat ../rime-emoji/opencc/*.txt opencc/*.txt | opencc -c t2s.json | uniq > symbols.txt

# 开始生成词典
ln -sf "../rime-essay/essay.txt" .
ln -sf "../chinese-dictionary-3.6million/词典360万（个人整理）.txt" .
ln -sf "../rime-pinyin-simp/pinyin_simp.dict.yaml" .
../src/clover-dict-gen.py --minfreq="$minfreq"
while read -r file; do
  echo "转换 $file"
  ../src/thuocl2rime.py "$file"
done < <(find ../THUOCL/data -type f -name 'THUOCL_*.txt')
cp ../src/sogou_new_words.dict.yaml .
../libscel/scel.py >> sogou_new_words.dict.yaml

# 生成 data 目录
mkdir -p ../data
cp ../src/*.yaml ../data
mv clover.*.yaml THUOCL_*.yaml sogou_new_words.dict.yaml ../data

# 生成 opencc 目录
cd ../data
mkdir -p opencc
cp ../rime-emoji/opencc/* opencc
cp ../cache/opencc/* opencc

echo "开始构建部署二进制"
rime_deployer --compile clover.schema.yaml . /usr/share/rime-data
rm -rf build/*.txt || true
