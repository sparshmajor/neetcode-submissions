# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = node = ListNode()
        flag = True
        while flag:
            flag = False
            smallest_node = float('inf')
            smallest_index = -1
            for index, _list in enumerate(lists):
                if _list:
                    flag = True
                    if _list.val <= smallest_node:
                        smallest_node = _list.val
                        smallest_index = index

            if smallest_index != -1:
                node.next = lists[smallest_index]
                lists[smallest_index] = lists[smallest_index].next
                node= node.next
        return dummy.next