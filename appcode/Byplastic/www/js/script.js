$(document).ready(function () {

    // Initialize Firebase
//    var config = {
//        apiKey: "AIzaSyCL5q-TjV95iEESOvOmf419Ovhim6HmMU0",
//        authDomain: "gjden-ac410.firebaseapp.com",
//        databaseURL: "https://gjden-ac410.firebaseio.com",
//        storageBucket: "gjden-ac410.appspot.com",
//        messagingSenderId: "951073665617"
//    };
//    firebase.initializeApp(config);
//
//    console.log(firebase.database());
//    //    var dbRefObject = firebase.database().ref('userlist');
//    var dbRefObject = firebase.database().ref('list');
//    //const dbRefList = dbRefObject.child('hobbies');
//
//    //sync the value
//    //dbRefObject.on('value', snap => console.log(snap.val()));


//    dbRefObject.on('value', snap => {
//
//
//    });

    //submit_ref.on('value', gotData, showError);



    var diy_disp_card_list = '';
    diy_disp_card_list = populateDiyDispCards(diy_disp_card_list);


    var diyKart_card_list = '';

    var diy_disp_card_data_list = [];

    var count = 1;

//    console.log(snap.val());
//    snap.forEach(function (childSnapshot) {



    for(var i=0;i<3;i++){
     var tmp = {
            title: "",
            img_src: "img/Recycle/a" + count + ".jpg",
            price: "120",
            num: ""
        };

        count++;


        diy_disp_card_data_list.push(tmp);   
    }
        

        //            console.log(childData);

//    });
    //    preObject.innerHTML = JSON.stringify(snap.val(), null, 3);


    diyKart_card_list = populateKartCards(diyKart_card_list, diy_disp_card_data_list);
    $("#page5_target").html(diy_disp_card_list);
    $("#page6").html(diyKart_card_list);

    var params = {
        fields: 'id,note,link,image'
    };




    //    page5_target


    $("#listItemBtn").on("click", function () {

        $("#result").append("<div>" + $("#listText").val() + " is added!");
        //        $("#listText").val("");
        //        $("#listNum").val("");



    });




});

function populateKartCards(diyKart_card_list, diy_disp_card_data_list) {



    for (var i = 0; i < diy_disp_card_data_list.length; i++) {

        var tmp = diy_disp_card_data_list[i];

        var diy_disp_card_obj = '<div class="prod_listing_card">' +
            ' <img class="prod_listing_card_img" src="' + tmp["img_src"] + '" alt="" style="    width: 100%;">' +

            '<span class="prod_listing_card_price"> <i class="fa fa-inr" aria-hidden="true"></i>&nbsp;' + tmp["price"] + ' </span>' +

            ' <span class="prod_listing_card_num"> ' + tmp["num"] + ' </span>' +

            ' <div class="prod_listing_card_text">' +
            tmp["title"] +
            '  </div><div class="prod_listing_card_icon"><i class="fa fa-heart" aria-hidden="true"></i></div>' +
            ' </div><br>';

        diyKart_card_list = diyKart_card_list + diy_disp_card_obj;
    }


    return diyKart_card_list;
}


function populateDiyDispCards(diy_disp_card_list) {
    var diy_disp_card_data_list = [{
        title: "Cycle Clock",
        img_src: "img/Recycle/a10.jpg",
        desc: " Think of upcycling as recycling old items into much prettier pieces for your home. So before you chuck out that tired old stool or ditch your dated desk for a swanky new piece of furniture, stop and think about how your beloved pieces could be updated and re-used."
    }, {
        title: "Welcome Doors",
        img_src: "img/Recycle/a9.jpg",
        desc: " Think of upcycling as recycling old items into much prettier pieces for your home. So before you chuck out that tired old stool or ditch your dated desk for a swanky new piece of furniture, stop and think about how your beloved pieces could be updated and re-used."
    }, {
        title: "Paper Sheep",
        img_src: "img/Recycle/a8.jpg",
        desc: " Think of upcycling as recycling old items into much prettier pieces for your home. So before you chuck out that tired old stool or ditch your dated desk for a swanky new piece of furniture, stop and think about how your beloved pieces could be updated and re-used."
    }]


    for (var i = 0; i < diy_disp_card_data_list.length; i++) {

        var tmp = diy_disp_card_data_list[i];

        var diy_disp_card_obj = '<div class="diy_disp_card" >' +

            '<div class="diy_disp_card_title" style="">' +

            tmp["title"] +

            ' </div>' +

            '  <img src="' + tmp["img_src"] + '" alt="" class="diy_disp_card_img" style="    width: 100%;">' +

            '   <div class="diy_disp_card_desc">' +

            tmp["desc"] +

            ' </div>' +

            '</div><br>';

        diy_disp_card_list = diy_disp_card_list + diy_disp_card_obj;
    }


    return diy_disp_card_list;
}
