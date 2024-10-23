function reset(){
    document.getElementById("form").reset()
    document.getElementById("bookId").value = ""
}
function save(){
    let read = document.getElementById("bookComplete")
    if(read.checked == true){
        //alert('READ')
       bookList = JSON.parse(localStorage.getItem('listItem3')) ?? []
        var id 
        bookList.length != 0 ? bookList.findLast((item)=> id = item.id) : id = 0
        
        if(document.getElementById('bookId').value){
            bookList.forEach(value => {
                if(document.getElementById('bookId').value == value.id){
                    value.title = document.getElementById('bookTitle').value,
                    value.author = document.getElementById('bookAuthor').value,
                    value.year = document.getElementById('bookYear').value,
                    value.isComplete = 1
                }
            })
        }
        else{
            var item = {
                id : id +1,
                title:document.getElementById('bookTitle').value,
                author:document.getElementById('bookAuthor').value,
                year:document.getElementById('bookYear').value,
                isComplete:1
            }
            bookList.push(item)
        }
        localStorage.setItem('listItem3', JSON.stringify(bookList))
    }
    //When the checkbox is not checked
    else{
        //var booklist2 = []
        bookList2 = JSON.parse(localStorage.getItem('listItem4')) ?? []
        var id
        bookList2.length !=0 ? bookList2.findLast((item) => id=item.id): id = 0
        if(document.getElementById('bookId').value){
            bookList2.forEach(value=>{
                if(document.getElementById('bookId').value == value.id){
                    value.title = document.getElementById('bookTitle').value
                    value.author = document.getElementById('bookAuthor').value
                    value.year = document.getElementById('bookYear').value
                    value.isComplete = 0
                }
            })
            document.getElementById('bookId').value=''
        }
        else{
            var item = {
                id:id+1,
                title:document.getElementById('bookTitle').value,
                author:document.getElementById('bookAuthor').value,
                year:document.getElementById('bookYear').value,
                isComplete:0
            }
            bookList2.push(item)
        }
        localStorage.setItem('listItem4', JSON.stringify(bookList2))
    }
    showData()
    document.getElementById('form').reset()
}

function showData(){
    var table = document.getElementById('unreadTable')
    table.innerHTML=``
    bookList = JSON.parse(localStorage.getItem('listItem4')) ?? []
    bookList.forEach(function(value, i) {
        table.innerHTML += `
        <tr>
            <td>${i+1}</td>
            <td>${value.title}</td>
            <td>${value.author}</td>
            <td>${value.year}</td>
            <td><button class="btn btn-sm btn-warning" 
                    onclick="read(${value.id}, '${value.title}', '${value.author}',${value.year})">
                    <i class="fa fa-check"></i>
                </button>
            </td>
            <td><button class="btn btn-sm btn-success"
                 onclick="find(${value.id})" >
                    <i class="fa fa-edit"></i>
                </button>
            </td>
            <td><button class="btn btn-sm btn-danger" 
                onclick = "removeData(${value.id})">
                     <i class="fa fa-trash"></i>
                </button>
            </td>
         </tr>   `
    })
    //console.log('TABLE',table.innerHTML)
    var table2 = document.getElementById('readTable')
    table2.innerHTML=``
    bookList2 = JSON.parse(localStorage.getItem('listItem3')) ?? []
    bookList2.forEach(function(value2, i) {
        //var table2 = document.getElementById('readTable')
        table2.innerHTML += `
        <tr>
            <td>${i+1}</td>
            <td>${value2.title}</td>
            <td>${value2.author}</td>
            <td>${value2.year}</td>
            <td><button class="btn btn-sm btn-warning" >
                    <i class="fa fa-check"></i>
                </button>
            </td>
            <td><button class="btn btn-sm btn-success" >
                    <i class="fa fa-edit"></i>
                </button>
            </td>
            <td><button class="btn btn-sm btn-danger" >
                     <i class="fa fa-trash"></i>
                </button>
            </td>
         </tr>   `
    })
}

function read(id1, title1, author1, year1){
    if(id1){
        var item=[{
            id: id1,
            title: title1,
            author: author1,
            year: year1,
            isComplete: 1
        }]
        bookList = JSON.parse(localStorage.getItem('listItem3')) ?? []
        books = item.concat(bookList)
        localStorage.setItem('listItem3', JSON.stringify(books))
    }
    bookList4 = JSON.parse(localStorage.getItem('listItem4')) ?? []
    bookList4 = bookList4.filter(value => {
        return value.id != id1
    })
    localStorage.setItem('listItem4', JSON.stringify(bookList4))
    showData()
}

function find(id1){
   //console.log(id1)
    bookList = JSON.parse(localStorage.getItem('listItem4')) ?? []
    bookList.forEach(value => {
        //console.log(value.id)
        if(value.id == id1){
            document.getElementById('bookId').value = id1
            document.getElementById('bookTitle').value = value.title
            document.getElementById('bookAuthor').value = value.author
            document.getElementById('bookYear').value = value.year
        }
    })
}

function removeData(id1){
    bookList = JSON.parse(localStorage.getItem('listItem4')) ?? []
    bookList = bookList.filter(value => {
        return value.id != id1
    })
    localStorage.setItem('listItem4', JSON.stringify(bookList))
    showData()
}