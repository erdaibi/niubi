class CommodityModel:
    def __init__(self, cid, name, price):
        self.cid = cid
        self.name = name
        self.price = price


class CommodityView:
    def __init__(self):
        self.controlle = CommodityController()

    def display_menu(self):
        print("1) 获取商品信息")
        print("2) 显示商品信息")
        print("3) 删除商品信息")
        print("4) 修改商品信息")
        print("5) 显示最贵商品信息")

    def select_menu(self):
        while True:
            try:
                item = int(input("请输入选项:"))
                if item == 1:
                    self.input_commoditys()
            except:
                print("输入有误")



    def input_commoditys(self):
        name = input("请输入商品名:")
        cid = int(input("请输入商品编号:"))
        price = float(input("请输入商品价格:"))
        comd = CommodityModel(cid, name, price)
        self.controlle.add_commoditys(comd)


class CommodityController:
    def __init__(self):
        self.list_comd = []
        self.comd_target = 1001

    def add_commoditys(self, comd_target):
        self.comd_target += 1
        self.list_comd.append(comd_target)


# 测试添加商品功能
c = CommodityView()
c.display_menu()
c.select_menu()
