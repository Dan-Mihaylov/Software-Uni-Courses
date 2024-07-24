function solution  (nums) {

    let longestIncreasing = 1;
    let longestDecreasing = 1;

    let currIncreasing = 1;
    let currDecreasing = 1;

    for (let i = 0; i < nums.length - 1; i++){

        if(nums[i] > nums[i + 1]) {
            currDecreasing += 1;
            longestDecreasing = Math.max(longestDecreasing, currDecreasing);
            currIncreasing = 1;
        } else if (nums[i] < nums[i + 1]) {
            currIncreasing += 1;
            longestIncreasing = Math.max(longestIncreasing, currIncreasing);
            currDecreasing = 1;
        } else {
            currIncreasing = 1;
            currDecreasing = 1;
        }
    }

    return Math.max(longestIncreasing, longestDecreasing);
    
}


console.log(solution([3, 2]));
