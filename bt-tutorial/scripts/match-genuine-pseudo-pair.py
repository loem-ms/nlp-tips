import argparse

def match(genuine, pseudo, nbest, output_dir):
    with open(genuine, 'r') as f_g, open(pseudo, 'r') as f_p:
        genuine_text = f_g.readlines()
        pseudo_hyp_text = f_p.readlines()

    src_tgt_pairs = [(pseudo_hyp_text[i], genuine_text[i//5]) for i in range(len(pseudo_hyp_text))]
    with open(output_dir+'/bt.source.txt', 'w') as f_s, open(output_dir+'/bt.target.txt', 'w') as f_t:
        f_s.writelines([pair[0] for pair in src_tgt_pairs])
        f_t.writelines([pair[1] for pair in src_tgt_pairs])

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--genuine')
    parser.add_argument('--pseudo')
    parser.add_argument('--nbest')
    parser.add_argument('--output-dir')
    args = parser.parse_args()
    match(args.genuine, args.pseudo, args.nbest, args.output_dir)