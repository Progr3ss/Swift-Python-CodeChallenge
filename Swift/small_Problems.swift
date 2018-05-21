

//The Fibonacci sequence 

/*
Fibonacci sequence: is a series of numbers such that any number except for the first and the second,
is the sum of the previous two. 

0,1,1,2,3,5,8,13....


Recursive: A recursive function is a function that calls
itself. 

*/

func fib1(n: UInt) -> UInt {

   return fib1(n: n-1) + fib1(n:n-2)
}

//We use UInt instead of Int beacuse the fibonacci sequence does not exit in the real of negative integers. 
//The function will run forever without returning a final result. we call lsuch
//a circumstance infinite recursion and it is analogous to an infinite loop
//We Never specified a base case. A base cse serves as a stopping point 
//print(fib1(n:5))


func fib2(n: UInt) -> UInt {
    //base case
    if(n < 2) {
      return n
    }
    // recursive cases
    return fib2(n: n-2) + fib2(n:n-1)


}

/*
fib2: returns 0. 
*/


print(fib2(n:10))


/*
Memoization to the Rescue 

Memoization is a technique in which we store the results of computational tasks when they are 
completed, so that when we need them again we can look them up instead of needing to compute 
them a second time

*/

//our old base case
var fibMemo: [UInt: UInt] = [0:0, 1:1]

func fib3(n: UInt) -> UInt{

  //our new base case
  if let result = fibMemo[n] {
    return result
  }else {
  //Memoization
  fibMemo[n] = fib3(n: n - 1) + fib3(n: n - 2)
  }
  return fibMemo[n]!
}



print("fib3 \(fib3(n: 50))")


func fib4(n: UInt) -> UInt {
  //special case
  if(n == 0){
    return n
  }
  //initially set to fib 0 
  var last: UInt = 0, next: UInt = 1

  for _ in 1..<n {
    (last, next) = (next, last + next)
  }
  return next 
}
