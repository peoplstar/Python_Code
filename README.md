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

| <img src="https://github.com/peoplstar/Python_Code/blob/main/random_ex/int(random()).PNG" width="80%" height="100%" alt="int(random())"></img> |<img src="https://github.com/peoplstar/Python_Code/blob/main/random_ex/randrange().PNG" width="85%" height="100%" alt="randrange()"></img>|<img src="https://github.com/peoplstar/Python_Code/blob/main/random_ex/randint().PNG" width="90%" height="100%" alt="randint()"></img>|   
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

####   **- For �ݺ���**
```python
for waiting_number in [0, 1, 2, 3, 4]:
    print("����ȣ : {0}".format(waiting_number))

for waiting_number in range(0, 5): 
    print("����ȣ : {0}".format(waiting_number))

    starbucks = ["���̾��", "�丣", "�׷�Ʈ"]
for customer in starbucks:
    print("{0}�մ�, Ŀ�ǰ� �غ�Ǿ����ϴ�.".format(customer))
```
####   **- While �ݺ���**
```python
customer = "�丣"
index = 5
while index >= 1: 
    print("{0}, Ŀ�ǰ� �غ� �Ǿ����ϴ�. {1}�� ���Ҿƿ�.".format(customer,index))
    index -= 1
    if index == 0:
        print("Ŀ�Ǵ� ���ó�еǾ����ϴ�.")

# continue, break
absent = [2, 5] 
no_book = [7]
for student in range(1, 11):
    if student in absent: # student�� absent �� ���� �Ǿ��ִٸ�
        continue 
    elif student in no_book:
        print("���� ���� �������. {0}�� �����Ƿ�".format(student))
        break
    print("{0}, å �о��.".format(student))
print("\n\n")
```
- `while ()` ���� ���ǽ��� False �϶� �ݺ� ����
- `continue`  ���� �ݺ����� �ǳʶ�
- `break` �ݺ��� ����

## - __02.12__ -
> **<h3>Function</h3>**
```python
# �⺻�� ����

def profile(name, age, main_lang):
    print("�̸� : {0}\t ���� : {1}\t �� ��� ��� : {2}".format(name, age, main_lang))

profile("���缮", 20, "���̽�")
profile("����ȣ", 25, "C���")
```
```python
# ���� ���� ���� ���� ���� �б�.

def profile1(name, age = 17, main_lang = "���̽�"):
    print("�̸� : {0}\t ���� : {1}\t �� ��� ��� : {2}".format(name, age, main_lang))

profile1("�ڸ��")
```
- ���ڸ� �⺻���� �����Ͽ� �̸��� �Ѱ��൵ ���డ��
```python
# ���� ���� 
def profile2(name, age, *main_lang): 
    print("�̸� : {0}\t ���� : {1}\t".format(name, age), end = " ") # end = " " ��� �� �ٹٲ��� �������� ����
    for lang in main_lang:
        print(lang, end = " ")
    print() # �ٹٲ�

profile2("���缮", 20, "Python", "Java", "C", "C++", "C#")
profile2("����ȣ", 23, "KOtiln", "Swift")
```
- `*main_lang` �� ���ڸ� ���� �� �Է� ���� �� ����
------
```python
gun = 10 # ���� ����

def checkprint(soldiers): # ���ٹ�
    gun = 20 # ------(1)
    gun = gun - soldiers # ���� ����
    print("[�Լ� ��] ���� �� : {0}".format(gun))

print("��ü �� : {0}".format(gun)) # ���� ���� '10 ���'
checkprint(2) # 2���� ��� �ٹ� ���� '18' ���
print("���� �� : {0}".format(gun)) # ���� ���� '10 ���'
```
- **��������** = `[`�Լ� �������� �̿밡�� `/` �Լ� ȣ�� �� ���� �Լ�ȣ�� `/` ���� �� �����`]`
- **��������** = `[`���α׷� ��𿡼��� ȣ�� ����`]`
- **---- (1)** ���� ���� ������ ����ϱ� ���ؼ��� `global gun`�� ���� ���� �տ� `global` �� ��� 
  
## - __02.13__ -
> **<h3>Standard In & Ounput</h3>**
```python
print("Python", "java", "C++", sep=",", end="?")  
print("������ �� ����������?")
```
- `sep` ���� ���� ���ڰ� ���� ó���� ���� 
- `end` ���� ���� ���ڿ� �������� ���� **default�� �ٹٲ�**
```python
scores = {"����":0, "����":50, "�ڵ�":100} # dictionary
for subject, score in scores.items(): # scores�� key �� subject, values �� score�� Ʃ�÷� ����
    print(subject.ljust(8), str(score).rjust(4), sep=":")
                                                          
```
- `ljust(8)` �� 8ĭ�� Ȯ���� �� �������� ����
- `rjust(4)` �� 4ĭ�� Ȯ���� �� ���������� ����
```python
# 001, 002, 003, 004, ...
for num in range(1, 21):
    print("����ȣ : " + str(num).zfill(3)) 
```
- `zfill(3)` 3���� ���� �� ���� �κ��� 0���� ä�� `[ zero fill ]`
```python
# �� �ڸ��� �������� �ΰ�, ������ ������ �ϵ�, �� 10�ڸ� Ȯ��
print("{0: >10}".format(500)) # ' ' : ����ó�� > : ������ ���� 10 : 10�ڸ� Ȯ��

# ����� �� + ǥ��, ������ �� - ǥ��
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# ���� �����ϰ�, ��ĭ�� _�� ä��
print("{0:_<-10}".format(-500))

# 3�ڸ����� ,ó�� +- ��ȣó��
print("{0:+,}".format(-1000000000))
print("{0:-,}".format(1000000000))

# �Ҽ��� ���
print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3)) # �Ҽ� ��°�ڸ����� ���
```
## - __02.16__ -
> **<h3>File Input</h3>**
```python
score_file = open("score.txt","w",encoding="utf8") 
print("���� : 0", file=score_file)
print("���� : 50", file=score_file)
score_file.close() # score.txt ������ �����Ǹ鼭 print �ش� ���ڿ��� �ؽ�Ʈ���Ͼȿ� ����
```
```python
score_file = open("score.txt", "a", encoding="utf8") 
score_file.write("���� : 80")
score_file.write("\n�ڵ� : 100")
score_file.close()
```
```python
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read()) # score.file�� �о� �ѹ��� ���
score_file.close()
```
- �������� ���� `W` , �б����� ���� `R` , ����� `A` ,  `encondig="utf8"` �� �Է����� ������ �ѱ� ���� ����
  
- `write()`�� ����� �� �ٹٲ��� �������� �ʴ´�.   
 ���� `\n `���Խ��������.

> **<h3>File Output</h3>**
```python
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line: # �о���� ������ ������
        break
    print(line, end="")
score_file.close()
```
```python
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # ��� line�� �о list ���·� ����
for line in lines:
    print(line, end="")
score_file.close()
```
- `print(line)`�� �̿� �� �� �� �� �а� Ŀ���� �ڵ����� ���� �ٷ� �̵�
- �� 2���� �ٹٲ��� �Ͼ�� �ǹǷ� `print(line, end="")` �� ��� 
> **<h3>`with`</h3>**
- �Ϲ� ����� �� `open()`,`close()` �ι��� ���� ����
- `with`������ �̿�� `close()`���� ������� �ʾ� ���ŷο��� ����

```python
with open("study.txt", "w", encoding="utf8") as study_file: 
    study_file.write("Python�� �����մϴ�.")

with open("study.txt", "r", encoding="utf8") as study_file1:
    print(study_file1.read()) 
```
- `as study_file` : �ҷ��� `study.txt` ���ϳ����� ���� `study_file`�� �ӽ� ����