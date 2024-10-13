let Student = { age : Natural, group : Text, name : Text }

let Group = Text

let groupPrefix = "ИКБО-"

let groupYear = "-20"

let makeGroup =
      λ(n : Natural) →
        groupPrefix ++ Natural/show n ++ groupYear

let groups =
      [ makeGroup 1, makeGroup 2, makeGroup 3, makeGroup 4, makeGroup 5
      , makeGroup 6, makeGroup 7, makeGroup 8, makeGroup 9, makeGroup 10
      , makeGroup 11, makeGroup 12, makeGroup 13, makeGroup 14, makeGroup 15
      , makeGroup 16, makeGroup 17, makeGroup 18, makeGroup 19, makeGroup 20
      , makeGroup 21, makeGroup 22, makeGroup 23, makeGroup 24
      ]

let students =
      [ { age = 19, group = makeGroup 4, name = "Иванов И.И." }
      , { age = 18, group = makeGroup 5, name = "Петров П.П." }
      , { age = 18, group = makeGroup 5, name = "Сидоров С.С." }
      , { age = 20, group = makeGroup 6, name = "Кузнецов К.К." }
      ]

let subject = "Конфигурационное управление"

in  { groups = groups, students = students, subject = subject }
