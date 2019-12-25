$('#carousel-example').on('slide.bs.carousel', function (e) {
    /*
        CC 2.0 License Iatek LLC 2018 - Attribution required
    */
    let $e = $(e.relatedTarget);
    let idx = $e.index();
    let itemsPerSlide = 5;
    let totalItems = $('.carousel-item').length;

    if (idx >= totalItems - (itemsPerSlide - 1)) {
        let it = itemsPerSlide - (totalItems - idx);
        for (let i = 0; i < it; i++) {
            // append slides to end
            if (e.direction == "left") {
                $('.carousel-item').eq(i).appendTo('.carousel-inner');
            } else {
                $('.carousel-item').eq(0).appendTo('.carousel-inner');
            }
        }
    }
});
// $(function () {
//     $(".test").click(function (e) {
//         pageurl = $(this).attr('href');
//         $.ajax({
//             url: pageurl,
//             cache: false,
//             beforeSend: function () {
//                 $('#loading').show();
//             },
//             complete: function () {
//                 $('#loading').hide();
//             },
//             success: function (html) {
//                 console.log(html);
//                 $('.left-content').html(html);
//             }
//         });
//         if (pageurl != window.location) {
//             window.history.pushState({path: pageurl}, '', pageurl);
//         }
//         return false;
//     });
// });

$('#id_image').on('change', function () {
    let fileName = $(this).val();
    $(this).next('.custom-file-label').html(fileName);
})

$('#id_images').on('change', function () {
    let files = $(this).prop("files")
    let names = $.map(files, function (val) {
        return val.name;
    });
    console.log(names.length);
    $(this).next('.custom-file-label').html(`Mục đã được chọn (${names.length})`);
})