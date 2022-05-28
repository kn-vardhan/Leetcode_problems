class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        ts = []
        answer = []
        values = []

        for t in transactions:
            ts.append(t.split(','))
        for i in range(len(ts)):
            if int(ts[i][2])  > 1000:
                answer.append(ts[i])
                continue
            name1 = ts[i][0]
            time1 = int(ts[i][1])
            city1 = ts[i][3]
            for j in range(len(ts)):
                if j != i:
                    name2 = ts[j][0]
                    time2 = int(ts[j][1])
                    city2 = ts[j][3]
                    if name1 == name2 and abs(time1-time2) <= 60 and city1 != city2:
                        answer.append(ts[i])
                        break

        for ans in answer:
            ans = ",".join(str(x) for x in ans)
            values.append(ans)
        return values


