class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

class Tree:
    def __init__(self, text):
        self.text = text
        self.root = self.build_huffman_tree()
        self.codebook = self.generate_codes()

    def build_huffman_tree(self):
        # Calculate frequency of each character
        frequency = {}
        for char in self.text:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

        # Create a list of nodes
        nodes = [Node(char, freq) for char, freq in frequency.items()]

        # Build the Huffman tree
        while len(nodes) > 1:
            # Sort nodes by frequency
            nodes.sort(key=lambda x: x.freq)
            
            # Pick two smallest nodes
            left = nodes.pop(0)
            right = nodes.pop(0)
            
            # Create a new internal node with these two nodes as children
            merged = Node(None, left.freq + right.freq)
            merged.left = left
            merged.right = right
            
            # Add the new node to the list of nodes
            nodes.append(merged)
        
        return nodes[0]

    def generate_codes(self, node=None, prefix="", codebook=None):
        if codebook is None:
            codebook = {}
        if node is None:
            node = self.root
        if node.char is not None:
            codebook[node.char] = prefix
        else:
            self.generate_codes(node.left, prefix + "0", codebook)
            self.generate_codes(node.right, prefix + "1", codebook)
        return codebook

    def encode(self):
        return "".join(self.codebook[char] for char in self.text)

    def decode(self, encoded_text):
        decoded_text = []
        node = self.root
        
        for bit in encoded_text:
            if bit == '0':
                node = node.left
            else:
                node = node.right
            
            if node.char is not None:
                decoded_text.append(node.char)
                node = self.root
        
        return "".join(decoded_text)
    '''
    def plot_tree(self):
        pass
    '''
    def _preorder(self, node):
        nodes = []
        if node:
            nodes.append(node)
            nodes.extend(self._preorder(node.left))
            nodes.extend(self._preorder(node.right))
        return nodes

if __name__ == "__main__":
    userIn = input()
    text = userIn
    huffman_tree = Tree(text)
    encoded_text = huffman_tree.encode()
    decoded_text = huffman_tree.decode(encoded_text)
    
    print("Original text:", text)
    print("Encoded text:", encoded_text)
    print("Decoded text:", decoded_text)
    print("Codebook:", huffman_tree.codebook)
    # huffman_tree.plot_tree()
