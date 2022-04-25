#!-*-coding:utf-8

word = "friends"
print(word[-3:-1])
print(word[2:4])
phone_number = '1388-666-0006'
hiding_number = phone_number.replace(phone_number[:9], "*" * 9)
print(hiding_number)
search = "168"
num_a = "1355-168-0146"
num_b = "1680-133-1688"
print(f"168 is at {num_a.find(search)} to {num_a.find(search)+len(search)} of num_a")
print(f"168 is at {num_b.find(search)} to {num_b.find(search)+len(search)} of num_b")

# str.find(a)，获取a在字符串str中的位置，只返回找到的第一个
# 字符串中需要插入多个值的时候，可以用.format处理
print("168 is at {} to {} of num_b".format(num_b.find(search),num_b.find(search)+len(search)))

# 'b'、'r'、'u'、'f'在字符串前面的作用各不相同，分别表示如下：
# b：bytes，r：表示忽略转义符'\',u：表示使用unicode编码模式，常见于中文前面，f：在字符串内部加{}配合使用，可以放入表达式
