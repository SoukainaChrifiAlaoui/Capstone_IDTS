__author__ = 'Soukaina'

import IDTS.modules.Tree

#Creating the math model as a BTS
root = IDTS.modules.Tree.Node (15, 'Conditions')
root.insert(10, 'no order')
root.insert(20, 'order')
root.insert(8, 'no repetition')
root.insert(12, 'repetition')
root.insert(25, 'repetition')
root.insert(17, 'no repetition')
root.insert(4, '5')
root.insert(26, '1')
root.insert(18, '3')
root.insert(24, '2')
root.insert(11, '4')

#setting parents
root.is_root()
root.right.set_parent(root)
root.right.left.set_parent(root.right)
root.right.right.set_parent(root.right)
root.right.left.right.set_parent(root.right.left)
root.right.right.set_parent(root.right)
root.right.right.left.set_parent(root.right.right)
root.right.right.right.set_parent(root.right.right)
root.left.set_parent(root)
root.left.right.set_parent(root.left)
root.left.right.left.set_parent(root.left.right)
root.left.left.set_parent(root.left)
root.left.right.left.set_parent(root.left.right)
root.left.left.left.set_parent(root.left.left)

#Embadding the guidance inside the nodes
root.hint = "Did you consider order in this problem?"
root.right.hint = "Not quite yet! It is important to take order into account, but is repetition allowed or not?"
root.right.right.hint = "Not quite! order and repetition should both be considered in this problem, but is the number of repetitions constrained?"
root.right.left.hint = "Your logic is correct, just take a look again at your numbers"
root.right.right.right.hint = "Not quite yet. Both order and repetition should be considered in this problem, but look again at the constrains on repeated elements!"
root.right.right.left.hint = "Your logic is correct, just take a look again at your numbers"
root.right.left.right.hint = "Your logic is correct, just take a look again at your numbers"
root.left.hint = "Not quite! You are correctly deducing that order doesn't matter in this problem, but is repetition allowed or not?"
root.left.right.hint = "Your logic is correct, just take a look again at your numbers"
root.left.left.hint = "Your logic is correct, just take a look again at your numbers"
root.left.right.left.hint = "Your logic is correct, just take a look again at your numbers"
root.left.left.left.hint = "Your logic is correct, just take a look again at your numbers"



