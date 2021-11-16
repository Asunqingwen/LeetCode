from LinkList import Node


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        dumpy = head
        while dumpy:
            new_node = Node(dumpy.val, next=dumpy.next)
            dumpy.next = new_node
            dumpy = dumpy.next.next
        dumpy = head
        while dumpy:
            new_node = dumpy.next
            new_node.random = dumpy.random.next if dumpy.random else None
            dumpy = dumpy.next.next

        new_head = head.next
        dumpy = head
        while dumpy:
            new_node = dumpy.next
            dumpy.next = dumpy.next.next
            new_node.next = new_node.next.next if new_node.next else None
            dumpy = dumpy.next
        return new_head
