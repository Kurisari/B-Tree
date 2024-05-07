# B-Tree Implementation

This Python script provides an implementation of a B-Tree data structure. B-Trees are self-balancing search trees that maintain sorted data and allow for efficient insertion, deletion, and searching operations. This implementation supports insertion, deletion, searching, and traversal operations on the B-Tree.

## Authors

- [@Kurisari](https://www.github.com/kurisari)
- [@Nemesis1174](https://github.com/Nemesis1174)

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Table of Contents

- [B-Tree Implementation](#b-tree-implementation)
  - [Authors](#authors)
  - [License](#license)
  - [Table of Contents](#table-of-contents)
  - [B-Tree Structure](#b-tree-structure)
  - [Functionality](#functionality)
    - [Insertion](#insertion)
    - [Deletion](#deletion)
    - [Searching](#searching)
    - [Traversal](#traversal)
  - [Running Tests](#running-tests)

## B-Tree Structure

The B-Tree is composed of nodes, each containing keys and child pointers. The keys are stored in sorted order within each node. The B-Tree maintains balance by ensuring that every node (except the root) has at least `t-1` keys and at most `2t-1` keys, where `t` is a parameter passed during the initialization of the B-Tree.

## Functionality

### Insertion

The `insert` method allows for the insertion of a new key into the B-Tree. If the insertion causes a node to exceed the maximum number of keys, the tree undergoes a split operation to maintain balance.

### Deletion

The `delete` method removes a key from the B-Tree. Similar to insertion, deletion ensures that the tree remains balanced by merging or redistributing keys among nodes when necessary.

### Searching

The `search` method checks whether a given key exists in the B-Tree. It traverses the tree recursively, comparing keys until the desired key is found or determined to be absent.

### Traversal

The `traverse` method performs an in-order traversal of the B-Tree, printing out the keys in sorted order.

## Running Tests

The `run_tests` function contains several test cases to demonstrate the functionality of the B-Tree implementation. These test cases cover insertion, deletion, traversal, and searching operations.

To execute the test cases, simply run the script. The results of each test case will be displayed in the console output.
