BIN_DIR=$1
MODEL_DIR=$2
LOG_FILE=$3

fairseq-train $BIN_DIR \
--arch transformer \
--encoder-layers 4 \
--decoder-layers 4 \
--encoder-embed-dim 512 \
--decoder-embed-dim 512 \
--encoder-ffn-embed-dim 1024 \
--decoder-ffn-embed-dim 1024 \
--encoder-attention-heads 4 \
--decoder-attention-heads 4 \
--optimizer adam \
--adam-betas '(0.9, 0.98)' \
--clip-norm 0.0 \
--lr 5e-4 \
--lr-scheduler inverse_sqrt \
--warmup-updates 4000 \
--dropout 0.3 \
--weight-decay 0.0001 \
--criterion label_smoothed_cross_entropy \
--label-smoothing 0.1 \
--max-tokens 1024 \
--log-interval 100  \
--max-update 50000 \
--share-all-embeddings \
--keep-last-epochs 10 \
--seed 1 \
--save-dir $MODEL_DIR | tee $LOG_FILE