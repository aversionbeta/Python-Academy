
ggplot(data = mpg) + 
  geom_point(mapping = aes(x=displ, y=hwy, color=manufacturer))

ggplot(data = mpg) + 
  geom_point(mapping = aes(x=displ, y=hwy, color=manufacturer))+
  facet_grid(drv ~ cyl)

ggplot(data = mpg) + 
  geom_point(mapping = aes(x=displ, y=hwy, color=manufacturer))+
  facet_wrap(~class, nrow=3, ncol = 4)

ggplot(data = mpg) + 
  geom_point(mapping = aes(x=displ, y=hwy, size=cty))+
  facet_wrap(~class, nrow=3, ncol = 4)

ggplot(data = mpg) + 
  geom_point(mapping = aes(x=displ, y=hwy))

ggplot(data = mpg) + 
  geom_smooth(mapping = aes(x=displ, y=hwy, linetype=drv, color=drv),
  show.legend=FALSE)
  
ggplot(data = mpg) + 
  geom_smooth(mapping = aes(x=displ, y=hwy, group=drv))

ggplot(data = mpg) + 
  geom_point(mapping = aes(x=displ, y=hwy, color=class))+
  geom_smooth(mapping = aes(x=displ, y=hwy))

ggplot(data = mpg, mapping = aes(x=displ, y=hwy)) + 
  geom_point()+
  geom_smooth()

ggplot(data = mpg, mapping = aes(x=displ, y=hwy)) + 
  geom_point(mapping = aes(color=class))+
  geom_smooth(mapping = aes(linetype=drv))


ggplot(data = mpg, mapping = aes(x=displ, y=hwy)) + 
  geom_point(mapping = aes(color=class))+
  geom_smooth(
    data = filter(mpg, class=="subcompact"),
    se=FALSE
  )

ggplot(data = mpg, mapping = aes(x=displ, y=hwy, color=drv)) + 
  geom_point()+
  geom_smooth(se=FALSE)
  
