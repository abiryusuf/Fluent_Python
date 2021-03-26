# count letters from sentences
# 1
def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(count_letters('I am abir'))

# 2
groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

def total_price(basket):
    total = 0
    for item in basket:
        total += basket[item]
    return round(total,2)

print("Total price - {}".format(total_price(groceries)))
# 3
add_email = {
    "gmail.com": ["clark.kent", "diana.prince", "peter.parker"], 
    "yahoo.com": ["barbara.gordon", "jean.grey"], 
    "hotmail.com": ["bruce.wayne"]
    }

def email_list(domains):
    email = []
    for domain, users in domains.items():
        for user in users:
            email.append(user + "@" + domain)
    return email
print(email_list(add_email))