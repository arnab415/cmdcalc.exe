import sys
import argparse as ap

def calc(args):
    if args.o == "add":
        return args.f + args.s
    elif args.o == "sub":
        return args.f - args.s
    elif args.o == "mul":
        return args.f * args.s
    elif args.o == "div":
        return args.f / args.s
    elif args.o == "div":
        return args.f / args.s
    else:
        return "This is a calculator in cmd.Please enter the first number with argument --f (Number),and second number with --s (Number) and operation --o (add,sub,mul,div)"
if __name__ == '__main__':
        parser = ap.ArgumentParser()
        parser.add_argument("--f", type=float, default=1.0,
                            help=("Please enter first number."))
        parser.add_argument("--s", type=float, default=3.0,
                            help=("Please enter second number."))
        parser.add_argument("--o", type=str, default="",
                            help=("Please enter the operation."))


        args = parser.parse_args()
        sys.stdout.write(str(calc(args)))