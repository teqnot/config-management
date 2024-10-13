{
    groups: std.map(function(i) "ИКБО-" + (i + 1) + "-20", std.range(0, 23)),
    students: [
      {
        age: 19,
        group: "ИКБО-4-20",
        name: "Иванов И.И."
      },
      {
        age: 18,
        group: "ИКБО-5-20",
        name: "Петров П.П."
      },
      {
        age: 18,
        group: "ИКБО-5-20",
        name: "Сидоров С.С."
      },
      {
        age: 20,
        group: "ИКБО-6-20",
        name: "Кузнецов К.К."
      }
    ],
    subject: "Конфигурационное управление"
  }
  