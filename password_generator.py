def random_passoword():
  import random
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(4,8)
  nr_symbols = random.randint(2,4)
  nr_numbers = random.randint(2,4)

  ran_let = [random.choice(letters) for char in range(1, nr_letters + 1)]
  ran_sym = [random.choice(symbols) for char in range(1, nr_symbols + 1)]
  ran_num = [random.choice(numbers) for char in range(1, nr_numbers + 1)]
  password_list = ran_let + ran_sym + ran_num
  random.shuffle(password_list)

  password = ""
  for char in password_list:
    password += char

  return password
