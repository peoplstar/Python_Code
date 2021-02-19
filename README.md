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

