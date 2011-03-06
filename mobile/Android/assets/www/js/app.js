Ext.setup({
    tabletStartupScreen: 'tablet_startup.png',
    phoneStartupScreen: 'phone_startup.png',
    icon: 'icon.png',
    glossOnIcon: false,
    onReady: function() {
      Ext.regModel('PaymentArea', {
                     fields: ['identifier', 'owner']
                   });

      var store = new Ext.data.JsonStore({
        model  : 'PaymentArea',
        sorters: 'owner',

        getGroupString : function(record) {
         return record.get('owner')[0];
        },

        data: [
          {identifier: 'tåg',   owner: 'SJ'},
          {identifier: 'Rob',     owner: 'Dougan'}
        ]
      });

      // var store = new Ext.data.JsonStore({
      //   url: 'http://localhost:8000/discovery/',
      //   root: 'images',
      //   fields: [
      //     'identifier', 'owner'
      //   ]
      // });
      // store.load();

      var list = new Ext.List(
        {fullscreen: true,

        itemTpl : '{owner} - {identifier}',
        grouped : true,
        indexBar: true,

        store: store
        });
      list.show();
    }
});