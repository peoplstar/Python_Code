# Python Training

`I'll share the link  i heard in the youtube lecture `

- ## Link : [Youtube](https://www.youtube.com/watch?v=kWiCuklohdY&t=15841s)

## - __02.08__ -
> **<h3>Variable</h3>**
```python
name = "��ź��"
animal = "������"
age = 4
hobbit = "��å"
is_adult = age >= 3 
```
- Python���� ���� ����� �ڷ����� **���**���� �ʴ´�.

```python
print("�츮��" + animal + "�� �̸���" + name + "����")
print(name + "�� " + str(age) + "���̸�," + hobbit + "�� ���� �����ؿ�") 
```
- print�� String���� �ν��ϱ⿡ age�� ���� �������� **str()**�� ����ȯ

> **<h3>Sentence</h3>**
```python
sentence = '���� �ҳ��Դϴ�'
print(sentence)
sentence2 = "this is python"
print(sentence2)
sentence3 = """ 
���� �ҳ��̰�,
this is python
""" 
```
- String �ʱ�ȭ�� `' '` , `" "` �� ����
- `"""` , `"""` �� �����ָ� __�ٹٲ� ����__���� �Է� ����
> **<h3>Slicing</h3>**
```python
secret_num = "000000-3111111"
print("���� : " + secret_num[7])
print("���� : " + secret_num[0:2])
print("�� : " + secret_num[2:4]) 

print("������� : " + secret_num[:6])
print("�� 7�ڸ� : " + secret_num[7:])
```
- **`[7]`** : �ε��� 7�� ���� ���
- **`[2:4]`** : �ε��� 2 ���� 4 ���� �� ���� ���
- **`[:6]`** : ó������ 6 ���� �� ���� ���
- **`[7:]`** : 7 ���� ������ ���

> **<h3>Formating</h3>**
```python
print("���� %d���Դϴ�." % 20) # printf("%d", operator)
print("���� %s���Դϴ�." % 20)
print("���� %s�� �����ؿ�" % "���̽�") #  printf("%s", operator) 

print("���� %s���� %s���� �����ؿ�." % ("�Ķ�", "����"))
print("���� {}���Դϴ�.".format(20)) # {}�� ���� �����õȴ�.
print("���� {}���� {}���� �����ؿ�.".format("�Ķ�","����"))
print("���� {0}���� {1}���� �����ؿ�.".format("�Ķ�","����"))
```
- ~~`print("���� {0}���� {1}���� �����ؿ�.".format("�Ķ�","����"))` �̰͸� ���~~

## - __02.09__ -
> **<h3>Math</h3>**
```python
print(1 != 3)
print(not (1 !=3))

print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))

print((3 > 0) or (7 < 5))
print((3 > 0) | (7 < 5))
```
- `!=` �� `not`�� True �϶� False, False �϶� True ���� ��ȯ

```python
print(int(random() * 10)) # 0 ~ 10 �̸��� ������ ������ ����
print(randrange(0,10)) # 0 ~ 10 �̸��� ������ �� ����
print(randint(0,9)) # 0 ~ 9 ������ ������ �� ����
```

|<img src="random_ex/int(random()).png" width="80%" height="100%" alt="int(random())"></img>|<img src="random_ex/randrange().png" width="85%" height="100%" alt="randrange()"></img>|<img src="random_ex/randint().png" width="90%" height="100%" alt="randint()"></img>|   
|:---:|:---:|:---:|
|`print(int(random() * 10))`|`print(randrange(0,10))`|`print(randint(0,9))`|

## - __02.10__ -
> **<h3>List</h3>**

```python
num_list = [10, 20, 30]
subway = ["���缮", "����ȣ", "�ڸ��"]
empty = list() 
empty = []
subway[-1]
```
- List�� �ε����� ���� �迭�� ����
- �ε��� -1 �� ���� ���� ������ �ε����� ����
  
> **<h3>List Function</h3>**
```python
subway.append("����")
subway.insert(1, "������")
num_list.sort()
num_list.reverse()
del num_list[2]
num_list.index(5)
```
`.append("temp")` : temp ���� ������ �ε����� �߰�   
`.insert(1,"temp")` : �ε��� 1 �� ��ġ�� temp �� ���� <mark> &</mark> �� ���� ���� ��� ���ڸ��� �з���   
`.sort()` : ������������ ����   
`.reverse()` : ����Ʈ�� ���θ� �������� ������ 
`del num_list[2]` : �ε����� 2�� �κ��� ���� ����   
`.index(5)` : ����Ʈ�� �ش� ���� ������ ��ġ ���� ��� <mark>&</mark> ������ ValueError

> **<h3> Dictionary</h3>** 
```python
cabinet = {3:"���缮", 100:"����ȣ"}
dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
cabinet["A-3"] = "���콺"
cabinet["C-23"] = "�е�"
```
- `{key : "value"}` �� �������� key�� value�� �� ����
- Dictionary ���� key�� ������ ���̱⿡ �ߺ��� �� ����.
- Key�� ���� ���ϸ� �ȵǱ⿡ Key���� List�� ��� �� �� ������     
Tuple�� ��� �����ϴ�.

####   **- Dictionary Key**
```python
print(cabinet[3]) # ���� Ű���� ��ȿ���� ���� �� �����߻�
print(cabinet.get(3)) # ���� Ű���� ��ȿ���� ���� �� None ���
print(cabinet.get(5, "��� ����")) # None ��� ���� ���� ����
print(3 in cabinet) # 3 �̶�� ���� cabinet �� ������ True ������ False
```

## - __02.11__ -
> **<h3>Conditional</h3>**
```python
weather = input("���� ������ ���? : ") 
temp = int(input("����� ���? : "))
    print("����� ì�⼼��")
elif weather == "�̼�����": # else if
    print("����ũ�� ì�⼼��")
else:
    print("�غ� �ʿ� �����")  

if 30 <= temp:
    print("�ʹ� ������")
elif 10 <= temp and temp < 30:
    print("�����ؿ�")
elif 0 <= temp < 10:
    print("������ ì�⼼��")
else: 
    print("���� �߿���")
```
- `and` = `&`  &nbsp;&nbsp;,&nbsp;&nbsp;  `or` = `|`
- input�� �׻� ���ڿ� `[` scanf , cin << `]` �� ���� 
- �׻� ���ڿ��� �ޱ⿡ `int(input())`�� ����ȯ�� �ʿ�

```python
for waiting_number in [0, 1, 2, 3, 4]:
    print("����ȣ : {0}".format(waiting_number))

for waiting_number in range(0, 5): 
    print("����ȣ : {0}".format(waiting_number))

    starbucks = ["���̾��", "�丣", "�׷�Ʈ"]
for customer in starbucks:
    print("{0}�մ�, Ŀ�ǰ� �غ�Ǿ����ϴ�.".format(customer))

```

<img src = "test.PNG">