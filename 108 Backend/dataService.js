
let mockCatalog=[
{
    id: "",
    title: "Black Heels",
    category: "Heels",
    price: 10.00,
    image: "blackheels.jpg",
},

{
    id: "",
    title: "Blue Heels",
    category: "Heels",
    price: 15.00,
    image: "blueheels.jpg",
},

{
    id: "",
    title: "Pink Heels",
    category: "Heels",
    price: 17.00,
    image: "pinkheels.jpg",
},

{
    id: "",
    title: "Green Ankle",
    category: "Heels",
    price: 16.00,
    image: "greenankle.jpg",
},

{
    id: "",
    title: "Green Booties",
    category: "Booties",
    price: 18.00,
    image: "greenbooties.jpg",
},

];

class DataService {

    getCatalog(){
    //get the catalog from the server
    //and return the list of products

    //testing only
    return mockCatalog;
    }
};

export default DataService;