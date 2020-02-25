def partition(arr,low,high):
    i = low -1
    pivot = arr[high]     # pivot

    for j in range(low , high):
        if pivot > arr[j]:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def minimumAbsoluteDifference(arr):
    quickSort(arr, 0, len(arr) - 1)
    cur_min = 2147483647
    for i in range(0, len(arr) -1):
        if(abs(arr[i] - arr[i + 1]) < cur_min) :
            cur_min = abs(arr[i] - arr[i + 1])
        if(abs(arr[i+1] - arr[i]) < cur_min) :
            cur_min = abs(arr[i+1] - arr[i])
    return cur_min

if(__name__=="__main__"):
    arr = [962226917,792624362,182480605,599605172,305625864,-81890988,672152087,-133378770,518530121,117194629,417799030,495022422,324358717,546432027,-964011537,-202521429,933382965,-636579333,-228322129,-56148272,765550188,-51728932,354422864,571036550,893033573,-632357224,230731537,957889690,-663303451,-681076766,850996627,796245935,-559647626,417083229,-555235827,-142871142,-265891342,216458754,-852793466,-629971246,-133880688,995384337,-792521943,276619340,391715447,369467242,-534628080,-529731961,159022806,12166614,-227099467,-340866802,-971186523,-292169152,-28963329,646052689,-3201546,-124238932,437046414,-992130998,46703511,290679769,29717534,-30334005,290115457,370682763,774552713,-405804880,416048754,594286847,718627398,-948572155,-955461030,-757111933,-217884128,-445764058,373256233,646756393,525687205,-71009539,-98598593,-361919562,-158639863,937486409,-180417430,916000073,-624472555,-568865371,-248713900,224013616,-741024587,88191350,-319295302,360654385,-973046747,-880171075,-301625980,642186024,123941140,-46393995]
    #quickSort(arr, 0, len(arr)-1)
    mini = minimumAbsoluteDifference(arr)
    print(str(mini))