import argparse
import random

def mix(
    genuine_source, genuine_target,
    pseudo_source, pseudo_target, 
    output_dir, with_tag=True
):
    all_text = []
    for file in [genuine_source, genuine_target, pseudo_source, pseudo_target]:
        all_text.append(open(file, 'r').readlines())
    
    if with_tag:
        all_text[2] = ['<Pseudo> '+x for x in all_text[2]]

    all_pairs = [(s, t) for s, t in zip(all_text[0]+all_text[2], all_text[1]+all_text[3])]
    random.shuffle(all_pairs)

    with open(output_dir+'/train.alt.mixed.bpe16K.en', 'w') as f_s, open(output_dir+'/train.alt.mixed.bpe16K.km', 'w') as f_t:
        f_s.writelines([pair[0] for pair in all_pairs])
        f_t.writelines([pair[1] for pair in all_pairs])


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--genuine-source')
    parser.add_argument('--genuine-target')
    parser.add_argument('--pseudo-source')
    parser.add_argument('--pseudo-target')
    parser.add_argument('--with-tag', default=False, action='store_true',
                            help='add <Pseudo> tag to pseudo source')
    parser.add_argument('--output-dir')
    args = parser.parse_args()
    mix(args.genuine_source, args.genuine_target,
        args.pseudo_source, args.pseudo_target,
        args.output_dir, args.with_tag
    )