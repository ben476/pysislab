import argparse

# example commands:

# list all nodes in the network
# python cli.py --list

# follow live data from node 1
# python cli.py --tail 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CLI for fetching data from the CRISiSLab seismometer network')
    parser.add_argument('--list', action='store_true', help='List all nodes in the network')
    parser.add_argument('--tail', type=int, help='Follow live data from node')
    args = parser.parse_args()

    if args.list:
        print("list all nodes in the network")
    elif args.tail:
        print("follow live data from node", args.tail)
    else:
        parser.print_help()