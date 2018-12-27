class HuffManNode:
    def __init__(self, value):
        self.left_child = None
        self.right_child = None
        self.value = value
        self.code = ""

def create_huffman_tree(input):
    node_list = []
    for i in input:
        node_list.append(HuffManNode(i))
    while len(input) > 1:
        left_child_value = input.pop(0)
        right_child_value = input.pop(0)

        left_child = HuffManNode(left_child_value)
        left_child.code = left_child.code + "1"
        right_child = HuffManNode(right_child_value)
        right_child.code = right_child.code + "0"
        node_value = left_child_value + right_child_value
        node = HuffManNode(node_value)
        node.left_child = left_child
        node.right_child = right_child

        for n in node_list:
            if n.value == node.left_child.value:
                node.left_child = n
                node.left_child.code = '1'
            if n.value == node.right_child.value:
                node.right_child = n
                node.right_child.code = '0'

        node_list.append(node)
        input.append(node_value)
        input = sorted(input)
    return node_list[-1]

tmp = []
def get_huffman_code(node):
    if node.left_child != None:
        node.left_child.code = node.left_child.code + node.code
        node.left_child.code = node.left_child.code + '1'
        get_huffman_code(node.left_child)
    elif node.right_child != None:
        node.right_child.code = node.right_child.code + node.code
        node.right_child.code = node.right_child.code + '0'
        get_huffman_code(node.right_child)
    else:
        tmp.append(node)
    return node

if __name__ == "__main__":
    # lis = [1,3,3,6,7,10,11]
    lis = [2,2,3,3,4,4,4,4,5,6,6,7,9,10]
    lis = sorted(lis)
    l = create_huffman_tree(lis)
    get_huffman_code(l)
    l =str()
    print(l + '1'+'0')
