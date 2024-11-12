var libro = {
  tiulo: "Las legiones",
  autor: "William Rodriguez",
  informacion: function () {
    return this.tiulo + "escrito por " + this.autor;
  },
};
console.log(typeof libro.informacion());
