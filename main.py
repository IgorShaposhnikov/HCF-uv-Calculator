class Column:
    def __init__(self, n: int, qn: int, un: int, vn: int) -> None:
        self.__n = n
        self.__qn = qn
        self.__un = un
        self.__vn = vn
    
    @property
    def n(self) -> int:
        return self.__n
    
    @property
    def qn(self) -> int:
        return self.__qn
    
    @property
    def un(self) -> int:
        return self.__un
    
    @property
    def vn(self) -> int:
        return self.__vn
    
    def __str__(self) -> str:
        n = str(self.__n)
        qn = str(self.__qn)
        un = str(self.__un)
        vn = str(self.__vn)
        return n + " " * (6 - len(n)) + "| " + qn + " " * (6 - len(qn) + 1) + "| " + un + " " * (6 - len(un) + 1) + "| " + vn


class Table:
    def __init__(self) -> None:
        self.__columns = []

    def add_colunm(self, column: Column) -> None:
        self.__columns.append(column)

    @property
    def columns(self) -> list:
        return self.__columns
    
    @property
    def column_count(self) -> int:
        return len(self.__columns)

    def __str__(self) -> str:
        return ''.join(['n     | qn     | un     | vn      \n', '-'*36, '\n'] + [str(column) + '\n' + "-"*36 + "\n" for column in self.__columns])


class ColumnDivision:
    def __init__(self, dividend, divisor) -> None:
        self.__dividend = dividend
        self.__divisor = divisor
        self.__divisor_count = 0
        self.__first_result = self.__calc()


    def __calc(self) -> int:
        if self.__divisor == 0:
            return 0
        self.__divisor_count = self.__dividend // self.__divisor
        return self.__dividend - self.__divisor * self.__divisor_count

    @property
    def dividend(self) -> int:
        return self.__dividend
    
    @property
    def divisor(self) -> int:
        return self.__divisor
    
    @property
    def first_result(self) -> int:
        return self.__first_result
    
    @property
    def divisor_count(self) -> int:
        return self.__divisor_count

    @staticmethod
    def calc(sender, array: list = []) -> list:
        if len(array) == 0:
            array.append(sender)

        sender: ColumnDivision
        newDivision = ColumnDivision(sender.divisor, sender.first_result)
        if not sender.first_result <= 0:
            array.append(newDivision)
            ColumnDivision.calc(newDivision, array)
        return array[:-1]
        
    def __str__(self) -> str:
        return str(self.__dividend) + " " + str(self.__divisor) + " " + str(self.__divisor_count) + " " + str(self.__first_result)


def main() -> None:
    dividend, divisor = map(int, input("НОД для: ").split())
    first_column_division = ColumnDivision(dividend, divisor)
    g = ColumnDivision.calc(first_column_division)
    mod = g[-1].first_result
    table = Table()
    for i, item in enumerate(g):
        item: ColumnDivision
        column: Column
        if table.column_count == 0: 
            column = Column(i + 1, item.divisor_count, 1, -item.divisor_count)
        elif table.column_count == 1:
            column = Column(
                i + 1, 
                item.divisor_count, 
                -item.divisor_count, 
                1 + table.columns[i - 1].qn * item.divisor_count
            )
        else:
            column = Column(
                i, 
                item.divisor_count, 
                table.columns[i - 2].un - table.columns[i - 1].un * item.divisor_count, 
                table.columns[i - 2].vn - table.columns[i - 1].vn * item.divisor_count
            )
        table.add_colunm(column)

    print(table)
    print("d =", mod)


if __name__ == '__main__':
    main()
