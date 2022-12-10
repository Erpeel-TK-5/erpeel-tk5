
const token = "Bearer 0a04e1e24d0f8378239582a5f78fc771c0a7bc0c59a5e125c05da47f81d51756662a4ded3c26e78fa033fca3d0d076863d48ac1b74d63a78b5ccd177ac55c9bc7c94692d962e10533d377963b151500a08629d83466843fae102f4784c9dfc3ddf880ee51abeba58fb02fe4fdb7e6f8387942c42391ac58c7b3f18bc0d5de275"
async function fetchPosts(nama) {
    const API_URL = `https://strapi-production-ef0a.up.railway.app/api/calendar-users/${nama}/?populate=*`
    const response = await fetch(`${API_URL}`, {headers:{
        'Authorization': token}
        },
        
    )
    let data = await response.json()
    calender(data.data.attributes.listEvent.data, data.data.attributes)
}
function calender(data, orangData) {
    let mapData = new Map()
    const database = new Map()
    for (let x in data) {
        let mulai = new Date(data[x].attributes.startDate)
        let tahunMulai = mulai.getFullYear()
        let bulanMulai = mulai.getMonth()
        let tahunBulan = "year-"+tahunMulai+""+"month-"+bulanMulai
        let tanggalMulai = mulai.getDate()
        let judul = data[x].attributes.title
        let kata = judul+" pukul "+mulai.getHours()+":"+mulai.getMinutes()
        if (mapData.has(tanggalMulai)) {
            mapData.get(tanggalMulai).push(kata)
        }
        else {
            mapData.set(tanggalMulai, [kata])
        }
        const lol = mapToObj(mapData)
        database.set(tahunBulan, JSON.stringify(lol))
        
    }
    function mapToObj(map){
        const obj = {}
        for (let [k,v] of map)
          obj[k] = v
        return obj
      }
    
    
    console.log(database)
    var that = this;
    var month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    var calenderData = {};
    var weekdays = ["Sun","Mon", "Tue", "Wed", "Thur", "Fri","Sat"];
     that.monthCombo = document.getElementById('month')
   that.yearCombo = document.getElementById('year');
    that.$from = document.getElementsByClassName('from-val')[0];
    that.$to = document.getElementsByClassName('to-val')[0];
    that.$eventName = document.getElementsByClassName('event-name')[0];
    that.$isPublic = document.getElementById('public')
    that.$isRecurring = document.getElementById('recurring')
    that.$notes = document.getElementsByClassName('notes')
    var currentYear = new Date().getFullYear();
    var startDay,endDay,tableRow, tableData;
    var calenderArray = [];
   //localStorage.setItem('year-'+currentYear+'month-', event);
    for (var i = 0; i < 12 ; i ++) {
        var option = document.createElement('option');
        option.value = i;
        option.innerHTML = month[i];
        option.className = 'dropdown-item';
        monthCombo.appendChild(option);
    }
    for(var j = new Date(0).getFullYear()  ; j <= currentYear + 10; j++) {
        var option = document.createElement('option');
        option.value = j;
        option.innerHTML = j;
        option.className = 'dropdown-item';
        yearCombo.appendChild(option);
        if(currentYear === j) {
            option.selected = 'selected';
        }
    }
    var table = document.createElement('table');
    table.id = "cTable";
    table.className = 'table';
    document.getElementById('table-div').appendChild(table);
    monthCombo.addEventListener('change', function () {
        calculateDays();
    });
    yearCombo.addEventListener('change', function () {
        calculateDays();
    });
    var today = new Date();
    document.getElementById('month').options.selectedIndex = today.getMonth();

    calculateDays();
    function clearModal() {
        that.$from.value = '';
        that.$to.value = '';
        that.$eventName.value = '';
        that.$isPublic.value = 'false'
        that.$isRecurring.value = 'false'
        that.$notes = ''
        that.modal.myModal.style.display = 'none';
    };
    function calculateDays() {
        var that = this;
       /* var monthAndYear = document.getElementById('month-and-year');
        monthAndYear.innerHTML = month[that.monthCombo.options.selectedIndex] + ', ' + that.yearCombo.selectedOptions[0].value;
       */ var storedData = JSON.parse(localStorage.getItem('year-'+that.yearCombo.selectedOptions[0].value+''+'month-'+that.monthCombo.options.selectedIndex));
       var keduaStoredData = null
       if (database.has('year-'+that.yearCombo.selectedOptions[0].value+''+'month-'+that.monthCombo.options.selectedIndex)) {
        keduaStoredData = JSON.parse(database.get('year-'+that.yearCombo.selectedOptions[0].value+''+'month-'+that.monthCombo.options.selectedIndex))
       }
       
       console.log(storedData)
       console.log(keduaStoredData)
        if(storedData) {
            calenderData = storedData;
        }
        else
            calenderData = {};
        document.getElementById('cTable').innerHTML = '';
        var th = document.createElement('tr');
        th.id = 'tr';
        th.className = 'thead-dark';
        document.getElementById('cTable').appendChild(th);
        for (var k = 0 ; k <weekdays.length ; k++) {
            var td = document.createElement('td');
            td.innerHTML = weekdays[k];
            document.getElementById('tr').appendChild(td);
        }
        calenderArray = [];
        var monthDays = new Date(parseInt(yearCombo.value), parseInt(monthCombo.value) + 1, 0).getDate();
        startDay = new Date(parseInt(yearCombo.value), parseInt(monthCombo.value), 1).getDay();
        endDay = new Date(parseInt(yearCombo.value), parseInt(monthCombo.value) + 1, 0).getDay();
        if (startDay !== 0) {
            for (var l = 0; l < startDay; l++) {
                calenderArray.push('b');
            }
        }
        for (var m = 1; m <= monthDays; m++) {
            calenderArray.push(m);
        }
        if (endDay !== 6) {
            for (var n = 0; n < 6 - endDay; n++) {
                calenderArray.push('b');
            }
        }
        
        for (var n = 0; n < calenderArray.length; n++) {
            if (n % 7 === 0) {
                tableRow = document.createElement('tr');
                tableRow.id = 'tr-' + (n / 7);
                tableRow.className = 'table-row';
                document.getElementById('cTable').appendChild(tableRow);
            }
            tableData = document.createElement('td');
            tableData.id = 'td-' + calenderArray[n];
            if (calenderArray[n] == 'b') {
                tableData.innerHTML = '';
            }
            else {
                tableData.innerHTML = calenderArray[n];
                if(calenderArray[n]===today.getDate() && parseInt(yearCombo.value) === today.getFullYear() && parseInt(monthCombo.value)=== today.getMonth()) {
                    tableData.classList.add('today');
                    tableData.innerHTML += '<br >' + '<div style = "padding-top: 30%">' + 'Today !!!' + '</div>';
                }
                if(calenderData[calenderArray[n]]) {
                    calenderData = storedData;
                    for (var p=0; p < calenderData[calenderArray[n]].length ; p++) {
                        var addEventDiv = document.createElement('div');
                        addEventDiv.id = 'event-on ' + calenderArray[n];
                        addEventDiv.classList.add('bg-card' ,'card');
                        addEventDiv.innerHTML += calenderData[calenderArray[n]][p];
                        tableData.appendChild(addEventDiv);
                    }


                }

            }
            tableData.addEventListener('click', function () {
                var span = document.getElementsByClassName("close")[0];
                span.onclick = function() {
                    modal.myModal.style.display = 'none';
                }
                that.modal = document.getElementsByClassName('modal');
                that.modal.myModal.style.display = 'block';
                that.selectedDate = parseInt(this.id.replace('td-', ''));
            });
            tableRow.appendChild(tableData);
        }

    }
    // TO set listener for each event card
    var allEvents  = document.querySelectorAll('.bg-card');
    allEvents.forEach(function (eventCard , index) {
        eventCard.addEventListener('click' , function () {
            console.log(eventCard, index);
        })
    })
    var saveBtn = document.getElementsByClassName('save-btn')[0];
    saveBtn.addEventListener('click', function () {
        var eventNameVal = that.$eventName.value;
        var fromVal = that.$from.value;
        var toVal = that.$to.value;
        var tan = that.yearCombo.selectedOptions[0].value+"-"+that.monthCombo.options.selectedIndex+"-"+that.selectedDate+" "
        var tanMul = new Date(`${tan}${fromVal}`)
        var tanAkh = new Date(`${tan}${toVal}`)
        console.log(that.$isPublic.value)
        console.log(that.$isRecurring.value)
        var pub = (that.$isPublic.value === 'true')
        var rec = (that.$isRecurring.value === 'true')
        var not = that.$notes.value
        var dataJson = {"data":
            {"title":eventNameVal,
            "startDate":tanMul.toJSON,
            "endDate":tanAkh.toJSON,
            "isPublic":pub,
            "isRecurring":rec,
            "notes":not,
            "dibuatOleh":orangData}
        }
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "https://strapi-production-ef0a.up.railway.app/api/events/?populate=*", true)
        xhr.setRequestHeader('Authorization', token);
        xhr.send(JSON.stringify({value:dataJson}))
        var content =  eventNameVal + ' ' + 'From'+ ' '+ fromVal +' '+ 'TO' + ''+ toVal +'<br>';
        if( !calenderData[selectedDate]) {
            calenderData[selectedDate] = [];
        }
        calenderData[that.selectedDate].push(content);
        window.localStorage.setItem('year-'+that.yearCombo.selectedOptions[0].value+''+'month-'+that.monthCombo.options.selectedIndex, JSON.stringify(calenderData));
       
       clearModal();
        calculateDays();

    });

    var closeBtn = document.getElementsByClassName('cancel-btn')[0];
    closeBtn.addEventListener('click', function () {
        clearModal.call(that);
    });
function eventHandLing(addEventDIv) {
    console.log(addEventDIv);
}

};
