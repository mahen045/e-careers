let sales = [
    { item: 'PS4 Pro', stock: 3, original: 399.99},
    { item: 'Xbox One X', stock: 1, original: 499.99, discount: 0.1},
    { item: 'Nintendo Switch', stock: 4, original: 299.99},
    { item: 'PS2 Console', stock: 1, original: 299.99, discount: 0.8},
    { item: 'Nintendo 64', stock: 2, original: 199.99, discount: 0.65}
] 

let updatedSalesTotal = salesTotal(sales)
console.log(updatedSalesTotal)

function salesTotal(sales){
    let updatedItems = 
    sales.map(inputSale => {
        let {original, discount=0.0} = inputSale
        inputSale['sale'] = (original - original * discount).toFixed(2)
        inputSale['total'] = (inputSale.sale * inputSale.stock).toFixed(2)
        return inputSale
    });
    return updatedItems
}
// Array: collection of values
// Object: collection of key-value pair
// Destructuring