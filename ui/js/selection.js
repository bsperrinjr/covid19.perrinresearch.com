$('select#states').change(function(){
    let state = $(this).children("option:selected").val();
    console.log($(this).children("option:selected").val());
    getData(state);
});
