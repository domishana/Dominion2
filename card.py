# coding=utf-8

from typing import List
from abc import ABCMeta, abstractmethod


class Card(metaclass=ABCMeta):
    def __init__(self, ename: str, jname: str, cost: int, _class: str, _type: List[str], set_name):
        self._ename = ename
        self._jname = jname
        self._cost = cost
        self._class = _class
        self._type = _type
        self._set_name = set_name


class TreasureCard(Card):
    def __init__(self, ename, jname, cost, _class, _type, set_name):
        super().__init__(ename, jname, cost, _class, _type, set_name)


class VictoryCard(Card):
    def __init__(self, ename, jname, cost, _class, _type, set_name):
        super().__init__(ename, jname, cost, _class, _type, set_name)


class CurseCard(Card):
    def __init__(self, ename, jname, cost, _class, _type, set_name):
        super().__init__(ename, jname, cost, _class, _type, set_name)


class ActionCard(Card):
    def __init__(self, ename, jname, cost, _class, _type, set_name):
        super().__init__(ename, jname, cost, _class, _type, set_name)


class ReactionCard:
    pass


class AttackCard:
    pass


class Copper(TreasureCard):
    def __init__(self):
        super().__init__("Copper", "銅貨", 0, "基本", ["財宝"], "基本")


class Silver(TreasureCard):
    def __init__(self):
        super().__init__("Silver", "銀貨", 3, "基本", ["財宝"], "基本")


class Gold(TreasureCard):
    def __init__(self):
        super().__init__("Gold", "金貨", 6, "基本", ["財宝"], "基本")


class Estate(VictoryCard):
    def __init__(self):
        super().__init__("Estate", "屋敷", 2, "基本", ["勝利点"], "基本")


class Duchy(VictoryCard):
    def __init__(self):
        super().__init__("Duchy", "公領", 5, "基本", ["勝利点"], "基本")


class Province(VictoryCard):
    def __init__(self):
        super().__init__("Province", "属州", 8, "基本", ["勝利点"], "基本")


class Curse(CurseCard):
    def __init__(self):
        super().__init__("Curse", "呪い", 0, "基本", ["呪い"], "基本")


class Garden(VictoryCard):
    def __init__(self):
        super().__init__("Garden", "庭園", 4, "王国", ["勝利点"], "基本")


class Adventurer(ActionCard):
    def __init__(self):
        super().__init__("Adventurer", "冒険者", 6, "王国", ["アクション"], "基本")


class Bureaucrat(ActionCard, AttackCard):
    def __init__(self):
        super().__init__("Bureaucrat", "役人", 4, "王国", ["アクション", "アタック"], "基本")


class Cellar(ActionCard):
    def __init__(self):
        super().__init__("Cellar", "地下貯蔵庫", 2, "王国", ["アクション"], "基本")


class Chancellor(ActionCard):
    def __init__(self):
        super().__init__("Chancellor", "宰相", 3, "王国", ["アクション"], "基本")


class Chapel(ActionCard):
    def __init__(self):
        super().__init__("Chapel", "礼拝堂", 2, "王国", ["アクション"], "基本")


class CouncilRoom(ActionCard):
    def __init__(self):
        super().__init__("Council Room", "議事堂", 5, "王国", ["アクション"], "基本")


class Feast(ActionCard):
    def __init__(self):
        super().__init__("Feast", "祝宴", 4, "王国", ["アクション"], "基本")


class Festival(ActionCard):
    def __init__(self):
        super().__init__("Festival", "祝祭", 5, "王国", ["アクション"], "基本")


class Laboratory(ActionCard):
    def __init__(self):
        super().__init__("Laboratory", "研究所", 5, "王国", ["アクション"], "基本")


class Library(ActionCard):
    def __init__(self):
        super().__init__("Library", "書庫", 5, "王国", ["アクション"], "基本")


class Market(ActionCard):
    def __init__(self):
        super().__init__("Market", "市場", 5, "王国", ["アクション"], "基本")


class Militia(ActionCard, AttackCard):
    def __init__(self):
        super().__init__("Militia", "民兵", 4, "王国", ["アクション", "アタック"], "基本")


class Mine(ActionCard):
    def __init__(self):
        super().__init__("Mine", "鉱山", 5, "王国", ["アクション"], "基本")


class Moat(ActionCard, ReactionCard):
    def __init__(self):
        super().__init__("Moat", "堀", 2, "王国", ["アクション", "リアクション"], "基本")


class MoneyLender(ActionCard):
    def __init__(self):
        super().__init__("Moneylender", "金貸し", 4, "王国", ["アクション"], "基本")


class Remodel(ActionCard):
    def __init__(self):
        super().__init__("Remodel", "改築", 4, "王国", ["アクション"], "基本")


class Smithy(ActionCard):
    def __init__(self):
        super().__init__("Smithy", "鍛冶屋", 4, "王国", ["アクション"], "基本")


class Spy(ActionCard, AttackCard):
    def __init__(self):
        super().__init__("Spy", "密偵", 4, "王国", ["アクション", "アタック"], "基本")


class Thief(ActionCard, AttackCard):
    def __init__(self):
        super().__init__("Thief", "泥棒", 4, "王国", ["アクション", "アタック"], "基本")


class ThroneRoom(ActionCard, AttackCard):
    def __init__(self):
        super().__init__("Throne Room", "玉座の間", 4, "王国", ["アクション"], "基本")


class Village(ActionCard):
    def __init__(self):
        super().__init__("Village", "村", 3, "王国", ["アクション"], "基本")


class Witch(ActionCard, AttackCard):
    def __init__(self):
        super().__init__("Witch", "魔女", 5, "王国", ["アクション", "アタック"], "基本")


class Woodcutter(ActionCard):
    def __init__(self):
        super().__init__("WoodCutter", "木こり", 3, "王国", ["アクション"], "基本")


class Workshop(ActionCard):
    def __init__(self):
        super().__init__("Workshop", "工房", 3, "王国", ["アクション"], "基本")
