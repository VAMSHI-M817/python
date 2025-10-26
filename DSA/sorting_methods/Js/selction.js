



function selectionSort(arr){
    n = arr.length
    for(i=0;i <= n-1; i++){
        min_index =i
        for(j=i+1;j<=n;j++){
            if(arr[j]<arr[min_index]){
                min_index=j
            }
        }
        let temp = arr[i]
        arr[i]= arr[min_index]
        arr[min_index]=temp
    }

    return arr
}

const res = selectionSort([64, 29, 21, 25, 87, 45])

console.log(res)