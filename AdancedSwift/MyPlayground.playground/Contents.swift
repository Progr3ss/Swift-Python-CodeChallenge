//: Playground - noun: a place where people can play

import UIKit

//Error Handling is just another way to write an else-if statement to deal with error messages

//Design Error(1/3)
enum HeightError : Error {
    case maxHeight
    case minHeight
}

//Call Function (2/3)
func checkHeightError(height: Int) throws {
    if height > 200 {
        throw HeightError.maxHeight
    }else if height < 10 {
        throw HeightError.minHeight
    }else{
        print("Enjoy!")
    }
}

// Handle with Error(3/3)

do {
    try checkHeightError(height: 400)
}catch HeightError.maxHeight {
    print("You are too tall")
}catch HeightError.minHeight {
    print("you are too short")
}


//Design Error
enum NameError: Error {
    case noName
}

class Course {
    var name: String
    
    init(name: String) throws{
        if name == "" {
            throw NameError.noName
        }else{
            self.name = name
            print("Hey, you've created an object!")
        }
    }
}

do {
    let myCourse = try Course(name: "learn Swift with martin")
}catch NameError.noName{
    print("make sure enter your name please")
}



//Type Cast
let label = UILabel() as UIView

// Design Class
class Human {
    func introduce()  {
        print("Hi, I'm a human ")
    }
}

// Design Subclass
class African : Human {
    func SingSong()  {
        "Mu re shan"
    }
}


let martin = African()
martin.introduce()
martin.SingSong()

// Type Casting
let newMartin = martin as Human
newMartin.introduce()

// as --> upcating (Always works)

class Japanese: Human {
    func doNinja()  {
        print("Shh....")
    }
}

//Upcating with Normal/Common types
var name =  "Bob" as Any
var number = 20 as Any


var anyArray = [name,number]

//Downcasting only occurs after upcasting
//Downcastign --> specific


//Downcasting
// Explicit/Force Downcasting

let newValue = anyArray[1] as! Int // normal type
//let anotherValue = anyArray[1] as! String  // fail

//Implicit Downcasting (Safe)
let newImValue = anyArray[0] as? Int
let newImNewValue = anyArray[1] as? Int





