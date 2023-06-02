mypost=[
    {
    "title":"Post 1",
    "content":"Hello this is post 1 and lorem lypsm lyosmsm",
    "id":1
    },
    {
    "title":"Post 2",
    "content":"Hello this is post 1 and lorem lypsm lyosmsm",
    "id":2
    },
    {
    "title":"Post 3",
    "content":"Hello this is post 1 and lorem lypsm lyosmsm",
    "id":3
    },
    {
    "title":"Post 4",
    "content":"Hello this is post 1 and lorem lypsm lyosmsm",
    "id":4
    }
]

idd=3

def find(id):
    for i,p in enumerate(mypost):
        if p['id']==id:
            # print(p["id"])
            print(i)
            return i

# print(find(1))
index=find(1)
mypost.pop(index)
print(index)
# print()