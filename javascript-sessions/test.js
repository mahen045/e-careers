let a = 10 //Redeclaration is restricted
a = 30 // Reassignment
//console.log(a)

let num1 = 10// Declaratiotenn
//name1="John" //Defined
//console.log(name1)

//console.log(num1++) //Post increment
//console.log(num1)
//console.log(++num1) //Pre increment
let num2 = 10

//console.log(num1 == num2 || num1>num2) // Strict comparision :compare alongwith data type

// if(num1 >= 10){
//     console.log("Greater than ten")
// }
// else{
//     console.log("Not greater than ten")
// }

//num1 > 10 ? console.log("greater than 10") : console.log("Not greater than ten")
//Print table of 2

let i = 1  // Initialization
while(i<=10){ //Condition
   // console.log(2*i)
    i++ // Increment
}

let str = "Education for all"
//console.log(str.toUpperCase())
//console.log(str.substring(10,13)) //for 

// Length of string = index+1

//create a loop and display the even numbers till 100

let names = ["Sam","Liam","Vince","Azhar"]

for(let name of names){
   // console.log(name)
}

names.length = 2
//console.log(names)
names.length = 4
//console.log(names)
//console.log(names.length)
//console.log(names[1])

//access last element
//console.log(names[names.length-1])
// console.log("Original Array:")
// console.log(names)
// names.pop()
// console.log("Modified Array after pop:")
// console.log(names)

// names.push("Michelle")
// console.log("Modified Array after push:")
// console.log(names)
//names[2] = "Florina"
//names[10] = "Asiya"
// console.log(names.length)
// console.log("Modified Array:")
// console.log(names)

let m = [10, 20]
catchM(m)
//console.log(m)

function catchM(n){
    n.push(30)
    
}

let arr = [12,8,24,13,15,7]
let evenNumbers = arr.filter(n => n%2==0) // Callback function
//console.log(evenNumbers)
//console.log(arr)
// function myFunction(n){
//     return n%2 == 0
// }

//  function max(p,q){
//      if(p>q){
//         return "p is greater"
//      }
//      else{
//         return "q is greater"
//      }
//  }

 let max = (p,q) => p>q ? "p is greater" : "q is greater"
let add = (p,q)=>p+q
//console.log(add(20,40))
//console.log(max(12, 62))


//Object literal
let employee = {
    empId:'E101',
    empName:'Dan',
    empAge:28,
    empSalary:50000,
    getSalary:function(){
        return this.empSalary*2
    }
}
//console.log('address' in employee)
employee.address='New York'
for(let emp in employee){
    console.log(employee[emp])
}
//console.log(employee.getSalary())
//console.log(employee)

//Function
//Method: function when used inside an object

//Class: class will be a blueprint for creating objects
class User {
    userName 
    userAddress 
    constructor(userName, userAddress){
        this.userName = userName
        this.userAddress = userAddress
    }
}
let user1 = new User('Tom', 'London')
let user2 = new User('Dave', 'New York')
//console.log(user1.userAddress)
//console.log(user2.userName)

//Vanila javascript
const posts = [{
    'title':'test', 'content':'Test1 content'
},{
    'title':'test2', 'content':'Test2 content'
}]

posts.forEach((post,index) =>{
    console.log(index)
    console.log(post.title)
})