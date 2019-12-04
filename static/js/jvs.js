function add_product(product_id) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function () {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
            var data = JSON.parse(xmlHttp.responseText)
            document.getElementById("count-items").innerHTML = data.count;
            var dom = document.getElementById(product_id);
            var quantity = Number(dom.getElementsByClassName("quantity")[0].textContent);
            if (quantity > 0) {
                quantity = quantity - 1;
                dom.getElementsByClassName("quantity")[0].innerHTML = quantity;
            }
            ;
            if (quantity == 0) {
                dom.getElementsByTagName("button")[0].disabled = true;
                dom.getElementsByClassName("quantity")[0].style.backgroundColor = "#b21f2d";
            }
            ;
            alert(data.mess);
        }
    }

    const isConfirm = confirm("Bạn có chắc muốn thêm sản phẩm");
    if (!isConfirm) {
        return;
    }
    xmlHttp.open("GET", "/add-product/?product_id=" + product_id, true);
    xmlHttp.send(null);
}


function checked_change() {
    var data = document.querySelector('input[name="position"]:checked').value;

    if (data == 'smart') {
        document.getElementById('chose-smart').style.display = "block";
        document.getElementById('chose-address').style.display = "none";
        document.getElementById("address").required = false;
        document.getElementById("phone_number").required = false;
        document.getElementById("delivery_time").required = false;

    } else {
        document.getElementById('chose-smart').style.display = "none";
        document.getElementById('chose-address').style.display = "block";
        document.getElementById("address").required = true;
        document.getElementById("phone_number").required = true;
        document.getElementById("delivery_time").required = true;
    }
    ;
};

function pay_checked() {
    var data = document.querySelector('input[name="pay"]:checked').value;
    if (data == 'money') {
        document.getElementById('chose-card').style.display = "none";
    } else {
        document.getElementById('chose-card').style.display = "block";
    }
    ;
};


function check_code() {
    var code = document.querySelector('input[name="code"]').value;
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function () {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
            var data = JSON.parse(xmlHttp.responseText);
            if (data.code == 1) {
                const isConfirm = confirm("Mã giảm giá hợp lệ, bạn có muốn sử dụng mã giảm giá không?");
                if (!isConfirm) {
                    return;
                }
                get_amount()
            } else {
                if (data.code == 0) {
                    alert('Mã giảm giá không hợp lệ');
                } else {
                    alert('Mã giảm đã có người sửa dụng');
                }
            }
        }
    }
    xmlHttp.open("GET", "/check_code/?code=" + code, true);
    xmlHttp.send(null);
}

function get_amount() {
    var code = document.getElementById('id_code').value;
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function () {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
            var data = JSON.parse(xmlHttp.responseText);
            document.getElementById("amount").innerHTML = moneyFormat(data.amount);
        }
    }
    xmlHttp.open("GET", "/get_amount", true);
    xmlHttp.send(null);
}


function get_price_of_maps() {
    var address = document.querySelector('textarea[name="address"]').value;
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function () {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
            var data = JSON.parse(xmlHttp.responseText);
            if (data.googlemaps.status == "OK") {
                document.getElementById("id_ship").value = moneyFormat(data.googlemaps.distance.value * 0);
                document.getElementById("amount").innerHTML = moneyFormat(data.amount + data.googlemaps.distance.value * 0);
            } else {
                alert("Sai địa chỉ vui lòng kiểm tra lại");
                document.getElementById("id_ship").value = "Free";
                document.getElementById("address").value = "";
                document.getElementById("amount").innerHTML = moneyFormat(data.amount);
            }
            // document.getElementById("ship").innerHTML = moneyFormat(data.distance.value);
        }
    }
    xmlHttp.open("GET", "/get_price_of_maps?address=" + address, true);
    xmlHttp.send(null);
}

function moneyFormat(n) {
    return String(n).replace(/(.)(?=(\d{3})+$)/g, '$1,') + "₫";
}