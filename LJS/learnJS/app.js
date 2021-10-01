const express = require('express')

const app =  express() 

// app.use(express.static('public'))

const os = require('os')
const hostname= os.hostname()
console.log(hostname)

// app.get('/', function(req , res ){
//     res.send('<h1>This is My Node_App</h1><h2>This is my Node_App</h2><h3>This is my Node_App</h3>')

// })

// app.get('/about', function(req , res ){
//     res.send({
//         Name : 'Star',
//         Technology : 'NodeJS'
//     })

// })

app.set('view engine','ejs')

app.get (  '/' , function(req,res){
    res.render('pages/index', { hostname : hostname , title : 'This is the home' })
} )

app.get (  '/star' , function(req,res){
    res.render('pages/about' , {title:'Its About'})
} )

app.listen(3000 , function() {
    console.log('Sever is activated on  3000')
})