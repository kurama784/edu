function send()
{
//Получаем параметры
var number_a_field = $('#number_a_field').val();
var number_b_field = $('#number_b_field').val();
var basic_field = $('#basic_field').val();
  // Отсылаем паметры
       $.ajax({
                type: "POST",
                url: "/equale",
                data: "number_a_field="+number_a_field+"&number_b_field="+number_b_field+"basic_field="+basic_field,
                // Выводим то что вернул PHP
                success: function(html) {
 //предварительно очищаем нужный элемент страницы
                        $("#answer").empty();
//и выводим ответ php скрипта
                        $("#answer).append(html);
                }
        });

}
