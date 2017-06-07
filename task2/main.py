class Event:
    def __init__(self, eventName, date, time):
        self.eventName = eventName
        self.date = date
        self.time = time


def loadFromFile(calendar):
    with open("events.txt", "r") as events:
        for event in events:
            first_space = event.find(" ")
            second_space = event.find(" ", first_space + 1)
            date = event[0:first_space].strip()
            time = event[first_space:second_space].strip()
            name = event[second_space:].strip()
            if date not in calendar:
                calendar[date] = []
                calendar[date].append(Event(name, date, time))

            else:
                calendar[date].append(Event(name, date, time))


def errorChecking(calendar):
    problemList = []
    for k, v in calendar.items():
        size = len(calendar[k])
        if size > 1:
            for i in range(size):
                start_first_index = calendar[k][i].time.find('-')
                start_first_time = calendar[k][i].time[0:start_first_index]
                end_first_time = calendar[k][i].time[start_first_index + 1:]
                #print(start_first_time, end_first_time)
                for j in range(1, size):
                    start_second_index = calendar[k][j].time.find('-')
                    start_second_time = calendar[k][j].time[0:start_second_index]


                    if int(start_second_time[0:1]) > int(start_first_time[0:1]) and int(start_second_time[0:1]) < int(end_first_time[0:1]):
                            problemList.append(calendar[k][i].eventName)
                            problemList.append(calendar[k][j].eventName)



    return problemList


def main():
    calendar = {}
    loadFromFile(calendar)
    problemList = errorChecking(calendar)
    print(problemList)

if __name__ == "__main__":
    main()
