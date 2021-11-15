import json


class Node():
    def __init__(self, name=None):
        self.name = name
        self.children = []


def toJSON(destList=[]) -> list:
    results = []
    if destList:
        for dest in destList:
            result = {}
            result['name'] = dest.name
            result['children'] = toJSON(dest.children)
            results.append(result)
    return results


def toObjectDict(srcList: str) -> str:
    destList = []
    for path in srcList:
        pathList = path.split('/')
        levelList = destList
        for name in pathList:
            if name != '':
                obj = None
                for level in levelList:
                    if level.name == name:
                        obj = level
                if not obj:
                    obj = Node(name)
                    levelList.append(obj)

                    if name == pathList[len(pathList) - 1]:
                        obj.children = []
                levelList = obj.children
    return destList


if __name__ == '__main__':
    srcList = ['/root/type1/1122',
               '/root/type1',
               '/root/type3',
               '/root/type4',
               '/root/type5',
               '/root/type1/a',
               '/root/type1/b',
               ]
    destList = toObjectDict(srcList)
    results = toJSON(destList)

    with open('test.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4, ensure_ascii=False)
