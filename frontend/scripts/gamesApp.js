
class Game {
    // Private fields
    #id; #name; #year; #platform;
    
    //Constructor
    constructor(id, name, year, platform) {
        this.#id = id;
        this.#name = name;
        this.#year = year;
        this.#platform = platform;
    }   

    //Getters
    get id() { return this.#id; }
    get name() { return this.#name; }
    get year() { return this.#year; }
    get platform() { return this.#platform; }
}

var vm = new Vue({
        el: "#gamesApp",
        data: {
            appName: "Games App",
            userName: "",
            selYear: "Year",
            selPlatform: "Platform",
            current_page: 0,
            games: []
        },
        created: async function f () {
            const response = await fetch("https://my-json-server.typicode.com/joseccampos/gamesLibrary/games");
            this.games = await response.json();
        },
        computed: {
            years: function () {
                var list = [];
                try{    
                    this.gamesPaginated[this.current_page].forEach(function (g) {
                        if (!(list.includes(g.year))) {
                            list.push(g.year);
                        }
                    });
                }catch (exception_var_2){}
                return list;
            },
            platform: function () {
                var list = [];
                try{
                    this.gamesPaginated[this.current_page].forEach(function (g) {
                        if (!(list.includes(g.platform))) {
                            list.push(g.platform);
                        }
                    });
                }catch (exception_var_2){}
                return list;
            },
            gamesFiltered: function() {
                var list = [];
                var selYear = this.selYear;
                var selPlatform = this.selPlatform;
                try{
                    this.gamesPaginated[this.current_page].forEach(function (g) {
                        if (selYear=="Year" && selPlatform=="Platform"){
                            list.push(g);
                        }else{
                            if (selYear=="Year"){
                                if (g.platform == selPlatform) {
                                    list.push(g);
                                }
                            }else{
                                if(selPlatform=="Platform"){
                                    if (g.year == selYear) {
                                        list.push(g);
                                    }
                                }else{
                                    if (g.year == selYear && g.platform == selPlatform) {
                                        list.push(g);
                                    }
                                }
                            }
                        }
                    });
                }catch (exception_var_2){}
                
                return list;
            },
            gamesPaginated : function(){
                var list = []
                var num_pages = Math.ceil(this.games.length/4);
                var i = 0;
                while(i<num_pages){
                    list.push([])
                    i += 1
                }
                i = 0
                var pag = -1
                this.games.forEach(function (g) {
                    
                    if(i==0){
                        pag += 1
                    }
                    
                    list[pag].push(g)

                    i += 1
                    i = i%4
                });
                return list
            }
        }
})