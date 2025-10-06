# CheckIn

Checkin é projeto desenvolvido com tecnologias modernas e estabelecidas dentro do mercado, com o objetivo
de criar um sistema de presença dentro de áreas de controle, de forma que facilite com que organizações -- desde 
o pequeno porte a empresas multinacionais -- consigam ter controle de seus funcionários dentro das instalações necessárias,
de forma que tenha maior seguridade e credibilidade nos sistemas de presença e permanencia de espaços controlados.

## Funcionamento

Temos que o funcionamento da nossa aplicação é focado em ter um controlador geral, várias subdistribuições existentes, e que 
os usuários não precisem constantemente recarregar e registrar novamente sua presença, já que a aplicação estará rodando em 
segundo plano. O registro constante do funcionário, seria feito por meio da sua geolocalização, onde o mesmo geraria pontos
de localidade de forma periódica, que seriam registrados dentro do banco de dados, e ao final da sua jornada, seriam computados
para ser possível ter a localidade final, inicial, e todo o percurso de deslocamento e ação desse determinado funcionário.

Para que o funcinamento seja dado de maneira completa e correta, temos que o mesmo deve ter o binário da aplicação web 
rodando em segundo plano no seu celular, e que durante o processo de inicio e término da jornada pelo menos, ele tenha algum tipo de
conexão com a internet, para que os registros da sua localização sejam enviados para processamento dentro do banco de dados.

Temos que a arquitetura padrão utilizada dentro do projeto de início, vai ser a monolítica, mas conforme as demandas e necessidades 
de maior escalabilidade, e maior flexibilidade no consumo de recursos forem aumentando, a estrutura pode ser modificada e migrada 
para que seja feita em uma arquiteutra de microsserviços.

## Cadastro
Temos que o cadastro dos administradores, áreas de controle, setores, jornadas, usuários e outros elementos, deve ser pelo gestor da organização,
ou alguma pessoa que tenha a permissão especial de fazer com que determinada ação possa ser feita, como um administrador de setor, ou adminsitrador 
de jornada.
Com isso, temos que toda organização vai ter uma pessoa responsável, a quem são atribuido características de administrador, e ela pode definir sub-administradores,
e pode definir usuários comuns a partir da necessidade de permissão de cada um dos níveis de cada um dos funcionários.




