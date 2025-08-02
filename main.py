from typing import Optional

def get_me_drink(total_count: Optional[]):
    print(type(total_count))
    for i in range(int(total_count)):
        
        print('gimme drink')

if __name__ == '__main__':
    get_me_drink(1)
    get_me_drink('1')
    get_me_drink(2.5)