
class Dog {
    constructor(name,breed,age = 0){
        this.name = name;
        this.breed = breed;
        this.age = age
    }
}

const grande  = new Dog('Grande','who knows', 5)
console.log(grande)