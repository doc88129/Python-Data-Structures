from list_node import *

def insert_sorted(head, value):
  tmp = head

  if not tmp:
    return ListNode(value)
  if tmp.val >= value:
    return ListNode(value, tmp)

  while tmp:
    if tmp.next == None or tmp.next.val >= value:
      new_node = ListNode(value, tmp.next)
      tmp.next = new_node
      break
    tmp = tmp.next

  return head

#pretty_print(insert_sorted(head_from_list([1,3,5]),6))
#pretty_print(insert_sorted(head_from_list([1,3]),0))