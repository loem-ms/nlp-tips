# Machine Translation with Fairseq

This is a note on machine translation task. We use English-Khmer translation task in this note.

## Dataset
We use Khmer-English parallel (ALT) corpus from [WAT 2020](http://lotus.kuee.kyoto-u.ac.jp/WAT/km-en-data/). Run the following commands to obtain the parallel data.

```
% wget http://lotus.kuee.kyoto-u.ac.jp/WAT/km-en-data/wat2020.km-en.zip
% unzip wat2020.km-en.zip
```

## Tokenization
We segment text in the parallel corpus into subword units. We use the byte pair encoding ([Sennrich et al., 2016b](https://aclanthology.org/P16-1162/)) to construct a vocabulary set with the size of 16K by sharing vocabulary between source and target sides. Please refer to [subword-nmt](https://github.com/rsennrich/subword-nmt) for detail.

```
% pip install subword-nmt
% cat wat2020.km-en/alt/train.alt.en wat2020.km-en/alt/train.alt.km | subword-nmt learn-bpe -s 16000 > wat2020.km-en/alt/bpe16K.codes
% for SET in train dev test; do \
subword-nmt apply-bpe -c wat2020.km-en/alt/bpe16K.codes < wat2020.km-en/alt/$SET.alt.en > wat2020.km-en/alt/$SET.alt.bpe16K.en
done
% for SET in train dev test; do \
subword-nmt apply-bpe -c wat2020.km-en/alt/bpe16K.codes < wat2020.km-en/alt/$SET.alt.km > wat2020.km-en/alt/$SET.alt.bpe16K.km
done
```

## Data Pre-processing
We can use `fairseq-preprocess` command to binarize the dataset.

```
% PARA_DIR=wat2020.km-en/alt
% BIN_DIR=wat2020.km-en.alt.bin
% bash scripts/preprocess.sh $PARA_DIR $BIN_DIR
```

## Model training
We use the de-facto standard neural encoder-decoder model, Transformer ([Vaswani et al., 2017](https://papers.nips.cc/paper/7181-attention-is-all-you-need)). Please refer to `scripts/train.sh` for detailed setting. Model architecture can be chosen/costumized with `--arch` option. For encoder-decoder architecture costumization, please read the official [documentation](https://fairseq.readthedocs.io/en/latest/tutorial_simple_lstm.html) of fairseq.


```
% BIN_DIR=wat2020.km-en.alt.bin
% MODEL_DIR=checkpoints
% LOG_FILE=wat2020.km-en.alt.transformer.log
% bash scripts/train.sh $BIN_DIR $MODEL_DIR $LOG_FILE
```

## Evaluation
We can generate translation of test set using `fairseq-generate`.
The last line of the output file includes BLEU score of generated translations. 

Averaging latest 10 checkpoints.

```
% python ../fairseq/scripts/average_checkpoints.py \
--inputs checkpoints \
--output checkpoints/checkpoint_avg.pt \
--num-epoch-checkpoint 10
```

```
% BIN_DIR=wat2020.km-en.alt.bin
% MODEL=checkpoints/checkpoint_avg.pt
% OUTPUT_FILE=test-output.txt
% bash scripts/generate.sh $BIN_DIR $MODEL $OUTPUT_FILE
```
We can also calculate BLEU score with `fairseq-score`.

```
% cat test-output.txt | grep '^H' | sed 's/^H\-//g' | sort -t ' ' -k1,1 -n | cut -f 3- > test-output.hyp.txt
% cat test-output.txt | grep '^T' | sed 's/^T\-//g' | sort -t ' ' -k1,1 -n | cut -f 2- > test-output.ref.txt
% fairseq-score -s test-output.hyp.txt -r test-output.ref.txt
```

We can translate raw text with trained model using `fairseq-interactive` command.

```
% BIN_DIR=wat2020.km-en.alt.bin
% MODEL_DIR=checkpoints
% fairseq-interactive \
--path $MODEL_DIR/checkpoint_avg.pt $BIN_DIR \
--beam 5 \
--source-lang en --target-lang km 
```