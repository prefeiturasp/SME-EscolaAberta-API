from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from core.models import Nucleo , Credits ,Debts

from debitos.api.serializers import DebitosSerializer
from creditos.api.serializers import CreditosSerializer



class NucleoSerializer(ModelSerializer):
    #debts = DebitosSerializer(many=True,read_only=True)
    #credits =CreditosSerializer(many=True,read_only=True)
    debts = DebitosSerializer(many=True)
    credits = CreditosSerializer(many=True)
    campoextra = SerializerMethodField()
    _id = SerializerMethodField()

    class Meta:
        model = Nucleo
        fields = (
             'id','_id', 'name', 'month', 'year','debts','credits','campoextra' ,'campoextra2'
        )
        read_only_fileds = ('debts','credits')

    def get_campoextra(self, obj):
        return 'tecnica de inserir campo extra - %s' %  obj.name

    def get__id(self, obj):
        return '%s' % obj.id

#-----------------insere dados tipo texto [Nested (aninhados)] -----------------------------------------------
    def cria_creditos(self,creditos, RegistroNoNucleo):
        for credito in creditos:
            cd = Credits.objects.create(**credito)
            RegistroNoNucleo.credits.add(cd)

    def cria_debitos(self,debitos, RegistroNoNucleo):
        for debito in debitos:
            debt = Debts.objects.create(**debito)
            RegistroNoNucleo.debts.add(debt)


    def create(self, validated_data):
        creditos = validated_data['credits']
        debitos = validated_data['debts']

        del  validated_data['credits']
        del validated_data['debts']
        RegistroNoNucleo = Nucleo.objects.create(**validated_data)

        self.cria_creditos(creditos,RegistroNoNucleo)
        self.cria_debitos(debitos, RegistroNoNucleo)
        pass
        return RegistroNoNucleo
#-------------------------------------------------------------------------------------------------------------

#-----------------insere dados tipo texto [Nested (aninhados)] -----------------------------------------------

    def update(self, instance, validated_data):

        credits_data = validated_data.pop('credits')
        creditos = (instance.credits).all()
        creditos = list(creditos)

        debts_data = validated_data.pop('debts')
        debitos = (instance.debts).all()
        debitos = list(debitos)

        instance.name = validated_data.get('name', instance.name)
        instance.month = validated_data.get('month', instance.month)
        instance.year = validated_data.get('year', instance.year)
        instance.save()
#--------------------------------------------------------------
        for crdREC in credits_data:
            if creditos:
                objCredito = creditos.pop(0)
                if objCredito:
                    objCredito.name = crdREC.get('name', objCredito.name)
                    objCredito.value = crdREC.get('value', objCredito.value)
                    objCredito.save()
            else:
                creditoNew = Credits.objects.create(**crdREC)
                instance.credits.add(creditoNew)
#---------------------------------------------------------------



        for dbtREC in  debts_data:
            if debitos:
                objDebito = debitos.pop(0)
                if objDebito:
                    objDebito.name = dbtREC.get('name', objDebito.name)
                    objDebito.value = dbtREC.get('value', objDebito.value)
                    objDebito.status = dbtREC.get('status', objDebito.status)
                    objDebito.save()
            else:
                debitoNew = Debts.objects.create(**dbtREC)
                instance.debts.add(debitoNew)


        instance.save()
        pass
        return instance
#-------------------------------------------------------------------------------------------------------------